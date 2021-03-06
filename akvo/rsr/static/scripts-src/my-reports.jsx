/** @jsx React.DOM */

// Akvo RSR is covered by the GNU Affero General Public License.
// See more details in the license.txt file located at the root folder of the
// Akvo RSR module. For additional details on the GNU license please see
// < http://www.gnu.org/licenses/agpl.html >.

var endpoints, i18n, Typeahead;

// CSRF TOKEN
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie("csrftoken");

var parameter_needed = function(report, parameter) {
    if (report == null) {
        return false;
    }
    for (var i = 0; i < report.parameters.length; i++) {
        if (report.parameters[i] === parameter) {
            return true;
        }
    }
    return false;
};

var get_display_value = function(id, options) {
    if (id == null) {
        return null;
    }
    var values = options.filter(function(option) {
        return option.id == id;
    });
    return values.length > 0 ? values[0].displayOption : null;
};

function initReact() {
    // Load globals
    Typeahead = ReactTypeahead.Typeahead;

    var OrganisationTypeahead = React.createClass({
        getInitialState: function() {
            return {
                placeholder: i18n.select_an_organisation
            };
        },

        componentDidMount: function() {
            if (this.props.organisationOptions.length === 1) {
                this.selectOrg(this.props.organisationOptions[0]);
                this.setState({
                    placeholder: this.props.organisationOptions[0].displayOption
                });
            }
        },

        selectOrg: function(org) {
            this.props.setOrganisation(org.id);
        },

        render: function() {
            return (
                <div className="form-group">
                    {React.createElement(Typeahead, {
                        placeholder: this.state.placeholder,
                        maxVisible: 10,
                        value: get_display_value(this.props.orgId, this.props.organisationOptions),
                        options: this.props.organisationOptions,
                        onOptionSelected: this.selectOrg,
                        displayOption: "displayOption",
                        filterOption: "filterOption",
                        customClasses: { input: "form-control" }
                    })}
                </div>
            );
        }
    });

    var SelectOrganisation = function(props) {
        var organisation;
        if (props.organisationOptions.length == 0) {
            organisation = <div />;
        } else if (props.organisationOptions.length == 1) {
            organisation = <p>{props.organisationOptions[0].displayOption}</p>;
        } else {
            organisation = (
                <div className="org-typeahead">
                    <OrganisationTypeahead
                        orgId={props.organisation}
                        organisationOptions={props.organisationOptions}
                        setOrganisation={props.setOrganisation}
                    />
                </div>
            );
        }
        return (
            <div id="choose-organisation">
                <label>{i18n.organisation}</label>
                {organisation}
            </div>
        );
    };

    var Reports = React.createClass({
        render: function() {
            var reports = this.props.reports,
                report_count = (reports && reports.length) || 0,
                row_count = Math.round(Math.ceil(report_count / 3)),
                row_indexes = Array.from(Array(row_count).keys()),
                col_indexes = Array.from(Array(3).keys()),
                self = this;
            return (
                <div className="rsrReports">
                    {row_indexes.map(function(row) {
                        return (
                            <div className="row" key={row}>
                                {col_indexes.map(function(col) {
                                    var index = row * 3 + col,
                                        report = reports[index];
                                    if (report === undefined) {
                                        return;
                                    }
                                    return (
                                        <Report
                                            disabled={self.props.disabled}
                                            orgId={self.props.organisation}
                                            report={report}
                                            key={report.id}
                                        />
                                    );
                                })}
                            </div>
                        );
                    })}
                </div>
            );
        }
    });

    var ReportFormatButton = React.createClass({
        onClick: function(e) {
            e.stopPropagation();
            this.props.download(this.props.format_name);
        },

        render: function() {
            const icon = this.props.icon,
                display_name = this.props.display_name,
                icon_class = "fa fa-" + icon,
                text = i18n.download + " " + display_name;
            return (
                <button
                    className="btn btn-default reportDown"
                    onClick={this.onClick}
                    disabled={this.props.disabled}
                >
                    <i className={icon_class} />
                    <span>&nbsp;&nbsp;</span>
                    <span>{text}</span>
                </button>
            );
        }
    });

    var Report = React.createClass({
        downloadReport: function(format) {
            var url = this.props.report.url,
                orgId = this.props.orgId,
                download_url = url.replace("{format}", format).replace("{organisation}", orgId);
            window.location.assign(download_url);
        },

        render: function() {
            var report = this.props.report,
                self = this,
                formats = report.formats.map(function(format) {
                    var icon = format.icon,
                        name = format.name,
                        display_name = format.display_name;
                    return (
                        <ReportFormatButton
                            disabled={self.props.disabled}
                            download={self.downloadReport}
                            icon={icon}
                            format_name={name}
                            display_name={display_name}
                            url={report.url}
                            key={format.name}
                        />
                    );
                });
            return (
                <div className="rsrReport col-sm-6 col-md-4">
                    <div className="reportContainer">
                        <div className="">
                            <h3 className="">{report.title}</h3>
                        </div>
                        <div className="reportDscr">{report.description}</div>
                        <div className="options">{formats}</div>
                    </div>
                </div>
            );
        }
    });

    var MyReportsApp = React.createClass({
        getInitialState: function() {
            return {
                reportOptions: [],
                organisation: null,
                organisationOptions: []
            };
        },

        componentDidMount: function() {
            this.getOptions(endpoints.user_organisations, "organisationOptions", this.processOrgs);
            this.getOptions(endpoints.reports, "reportOptions", this.processReports);
        },

        getOptions: function(endpoint, stateKey, processCallback) {
            var xmlHttp = new XMLHttpRequest();
            var url = endpoints.base_url + endpoint + "?format=json";
            var thisApp = this;
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == XMLHttpRequest.DONE && xmlHttp.status == 200) {
                    var newState = {};
                    if (processCallback === undefined) {
                        newState[stateKey] = JSON.parse(xmlHttp.responseText).results;
                    } else {
                        newState[stateKey] = processCallback(
                            JSON.parse(xmlHttp.responseText).results
                        );
                    }
                    thisApp.setState(newState);
                }
            };
            xmlHttp.open("GET", url, true);
            xmlHttp.send();
        },

        processOrgs: function(orgResults) {
            function getDisplayOption(short, long) {
                if (short === long) {
                    return short;
                }
                if (!long) {
                    return short;
                }
                return short + " (" + long + ")";
            }

            orgResults.forEach(function(o) {
                var newName = getDisplayOption(o.name, o.long_name);

                o.filterOption = o.name + " " + o.long_name;
                o.displayOption = newName;
            });

            // If only one organisation, also set the app state
            if (orgResults.length == 1) {
                this.setOrganisation(orgResults[0].id);
            }

            return orgResults;
        },

        processReports: function(reportResults) {
            // remove reports which have project as a parameter
            return reportResults.filter(function(report) {
                return report.parameters.indexOf("project") == -1;
            });
        },

        setReport: function(report) {
            this.setState({
                report: report
            });
        },

        setOrganisation: function(org) {
            this.setState({
                organisation: org
            });
        },

        render: function() {
            return (
                <div id="my-reports">
                    <h3>{i18n.my_reports}</h3>
                    <SelectOrganisation
                        organisationOptions={this.state.organisationOptions}
                        report={this.state.report}
                        organisation={this.state.organisation}
                        setOrganisation={this.setOrganisation}
                    />
                    <Reports
                        reports={this.state.reportOptions}
                        organisation={this.state.organisation}
                        disabled={!this.state.organisation}
                    />
                </div>
            );
        }
    });

    // Initialize the 'My reports' app
    ReactDOM.render(React.createElement(MyReportsApp), document.getElementById("container-fluid"));
}

var loadJS = function(url, implementationCode, location) {
    //url is URL of external file, implementationCode is the code
    //to be called from the file, location is the location to
    //insert the <script> element

    var scriptTag = document.createElement("script");
    scriptTag.src = url;

    scriptTag.onload = implementationCode;
    scriptTag.onreadystatechange = implementationCode;

    location.appendChild(scriptTag);
};

function loadAndRenderReact() {
    function loadReactTypeahead() {
        var reactTypeaheadSrc = document.getElementById("react-typeahead").src;
        loadJS(reactTypeaheadSrc, initReact, document.body);
    }

    function loadReactDOM() {
        var reactDOMSrc = document.getElementById("react-dom").src;
        loadJS(reactDOMSrc, loadReactTypeahead, document.body);
    }

    console.log("No React, load again.");
    var reactSrc = document.getElementById("react").src;
    loadJS(reactSrc, loadReactDOM, document.body);
}

document.addEventListener("DOMContentLoaded", function() {
    // Retrieve data endpoints and translations
    endpoints = JSON.parse(document.getElementById("data-endpoints").innerHTML);
    i18n = JSON.parse(document.getElementById("translation-texts").innerHTML);

    // Check if React is loaded
    if (
        typeof React !== "undefined" &&
        typeof ReactDOM !== "undefined" &&
        typeof ReactTypeahead !== "undefined"
    ) {
        initReact();
    } else {
        loadAndRenderReact();
    }
});
