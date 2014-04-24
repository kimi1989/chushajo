#!/usr/bin/env python
# encoding: utf-8
#########################################################################
# Copyright (c) 2011-2013 Kimi Jin                                      #
# Author(s): Kimi Jin <jinyinzhen@gmail.com>                            #
#########################################################################
import json
import urllib2


class MapQuestAPI:
    """
    Use mapquest API to get route and direction
    """

    def __init__(self, way_points):
        """
        Initialize the mapquest key, and the waypoints
        """
        self.key = 'Fmjtd%7Cluur2l6ynl%2Cba%3Do5-901xdu'
        import ipdb; ipdb.set_trace()
        try:
            if way_points[0].keys() == ['lat', 'lng']:
                self.way_points = way_points
        except Exception:
            print "Your way_points format is wrong, please input as: \n"
            print "[{'lat': xxx, 'lng': xxx}, {'lat': xxx, 'lng': xxx}, ...]"
            raise Exception
        self.url = self.__create_request_url()
        self.route_inform = json.load(urllib2.open(self.url))

    def __create_request_url(self):
        """
        create request url from direction or route
        """
        try:
            url = 'http://www.mapquestapi.com/directions/v2/route?key=YOUR_KEY_HERE&' \
                  'callback=renderAdvancedNarrative&ambiguities=ignore&avoidTimedConditions=false&' \
                  'doReverseGeocode=true&outFormat=json&routeType=fastest&timeType=1&enhancedNarrative=false&' \
                  'shapeFormat=raw&generalize=0&locale=en_US&unit=m&from=Start_point&End_point' \
                  'drivingStyle=2&highwayEfficiency=21.0'


            # Replace the key
            url = url.replace('YOUR_KEY_HERE', self.key)

            # Replace the Start_point
            start_point = str(self.way_points[0].values()).replace(' ', '').strip('[]')
            url = url.replace('Start_point', start_point)

            # Replace the End_point
            end_point = ''
            for way_point in self.way_points[1:]:
                end_point += 'to='
                end_point += str(way_point.values()).replace(' ', '').strip('[]')
                end_point += '&'
            url = url.replace('End_point', end_point)

            # url finishes
            return url

        except Exception:
            raise Exception

    def get_route(self):
        """
        get the route using MapQuest API
        """
        try:
            route = self.route_inform['route']
            return route

        except Exception:
            raise Exception


    def get_voice(self):
        """
        get the voice guidence direction
        """
        try:
            voices = self.route_inform['voices']
            return voices

        except Exception:
            raise Exception


