/*jslint browser: true*/
/*global $, jQuery, Handlebars, google*/

(function () {
    "use strict";

    // When included akvo-maps.js will query the page for elements with
    // class ".akvo_map". These elements should be generated by the maps
    // Django template tag. Each map element will have a div element and
    // a JavaScript litteral with data which are used to create a map with
    // corresponding locations from the RSR API

    var addMap, addPin, populateMap, mapOptions, prepareNextRequest, getResourceUrl;


    // For each .akvo_map element on the page, read options
    // and kick of the creation of a new map
    $(document).ready(function () {
        $('.akvo_map').each(function () {
            var mapId = $(this).attr('id');
            addMap({
                mapId: mapId,
                mapElement: document.getElementById(mapId),
                mapOpts: window[mapId]
            });
        });
    });


    // Creates the map with options and makes the initial AJAX request
    addMap = function (map) {
        $(map.mapElement).gmap(mapOptions(map.mapOpts.type)).bind('init', function () {
            $.getJSON(getResourceUrl(map), function (data) {
                populateMap(map, data);
            });
        });
    };


    // Creates resource URLS based on map options
    getResourceUrl = function (map) {
        var url = map.mapOpts.host + 'api/v1/',
        limit = 20;
        if (map.mapOpts.objectType === 'project') {
            return url + 'project/' + map.mapOpts.object + '/?format=jsonp&depth=1&callback=?';
        } else if (map.mapOpts.objectType === 'organisation') {
            return url + 'organisation/' + map.mapOpts.object + '/?format=jsonp&depth=1&callback=?';
        } else if (map.mapOpts.objectType === 'projects') {
            return url + 'project/?format=jsonp&depth=1&limit=' + limit + '&callback=?';
        } else if (map.mapOpts.objectType === 'organisations') {
            return url + 'organisation/?format=jsonp&depth=1&limit=' + limit + '&callback=?';
        }
    };



    // Populates the map with data
    populateMap = function (map, data) {
        var objects, objectType, pinTmpl;
        objectType = map.mapOpts.objectType;

        // Since API resources that list multiple objects (projects or organisations) include
        // a objects array we need to add the single project or organisation to an array. This Since
        // we want to keep using the same logic for both cases
        if (isNaN(map.mapOpts.object)) {
            objects = data.objects;
        } else {
            objects = [data];
        }

        pinTmpl = Handlebars.compile(
            '<div class="mapInfoWindow"' +
                'style="height:150px; min-height:150px; max-height:150px; overflow:hidden;">' +
                '<a class="small" href="{{url}}">{{title}}</a>' +
                '{{#if thumb}}' +
                    '<div style="text-align: center; margin-top: 5px;">' +
                        '<a href="{{url}}" title="{{title}}">' +
                            '<img src="{{thumb}}" alt="">' +
                        '</a>' +
                    '</div>' +
                '{{/if}}' +
                '</div>'
        );

        $.each(objects, function (i, object) {
            $.each(object.locations, function (k, location) {

                // Since organisation and projects have different data fields for
                // name, title and current_image and logo we need to make sure the location
                // object holds the wanted data
                if (objectType === 'organisation' || objectType === 'organisations') {
                    location.url = object.absolute_url;
                    location.title = object.name;
                    try {
                        location.thumb = object.logo.thumbnails.map_thumb;
                    } catch (e0) { location.thumb = ''; }

                } else {
                    location.url = object.absolute_url;
                    location.title = object.title;
                    try {
                        location.thumb = object.current_image.thumbnails.map_thumb;
                    } catch (e1) { location.thumb = ''; }
                }

                addPin(map, location, pinTmpl);
            });
        });

        // If we are rendering multiple objects and there are more objects to
        // grab from the API
        if (isNaN(map.mapOpts.object) && data.meta.next !== null) {
            prepareNextRequest(map, data.meta.next);
        }
    };

    // Add a single pin
    addPin = function (map, location, template) {
        var marker, objectType;
        marker = map.mapOpts.host + '/rsr/media/core/img/';
        objectType = map.mapOpts.objectType;

        if (objectType === 'organisation' || objectType === 'organisations') {
            marker = marker + 'redMarker.png';
        } else {
            marker = marker + 'blueMarker.png';
        }


        if (map.mapOpts.type === 'static') {
            $(map.mapElement).gmap('addMarker', {
                'position': new google.maps.LatLng(location.latitude, location.longitude),
                'clickable': false,
                'icon': marker,
                'bounds': true
            });
        } else {
            $(map.mapElement).gmap('addMarker', {
                'position': new google.maps.LatLng(location.latitude, location.longitude),
                'icon': marker,
                'bounds': true
            }).click(function () {
                $(map.mapElement).gmap('openInfoWindow', {
                    'content': template(location)
                }, this);
            });
        }
    };


    // Since we need to update the callback parameters we don't use the meta.next
    // but create a new resource url
    prepareNextRequest = function (map, resource) {
        var url = $.url(resource),
            urlTmpl = Handlebars.compile('{{host}}{{path}}?format=jsonp&depth=1&limit=' +
                '{{limit}}&offset={{offset}}&callback=?'),
            newUrl = urlTmpl({
                'host': url.attr('host'),
                'path': url.attr('path'),
                'limit': Number(url.param('limit')),
                'offset': Number(url.param('offset'))
            });
        $.getJSON(newUrl, function (data) {
            populateMap(map, data);
        });
    };


    // Static or dynamic map options
    mapOptions = function (mapType) {
        var options;
        if (mapType === 'static') {
            options = {
                'draggable': false,
                'mapTypeControl': false,
                'navigationControl': true,
                'scaleControl': false,
                'scrollwheel': false,
                'streetViewControl': false,
                'zoom': 2
            };
        } else {
            options = {
                'draggable': true,
                'mapTypeControl': true,
                'navigationControl': true,
                'scaleControl': true,
                'scrollwheel': false,
                'streetViewControl': false,
                'zoom': 2
            };
        }
        return options;
    };
}());
