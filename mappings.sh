#!/usr/bin/env bash

curl -XPOST $1:9200/$2

curl -XPOST $1:9200/$2/_mapping/$3 -d '
{
      "logs" : {
        "properties" : {
          "aircraft" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "aircraft_id" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "altitude" : {
            "type" : "long"
          },
          "arrival" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "arrived" : {
            "type" : "long"
          },
          "departure" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "iata_identity" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "icao_identity" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "last_update" : {
            "type" : "long"
          },
          "latitude" : {
            "type" : "double"
          },
          "longitude" : {
            "type" : "double"
          },
          "radar_id" : {
            "type" : "string"
          },
          "registration" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "reserved" : {
            "type" : "string"
          },
          "speed" : {
            "type" : "long"
          },
          "squawk_code" : {
            "type" : "string",
            "index":    "not_analyzed"
          },
          "angle" : {
            "type" : "long"
          },
          "vspeed" : {
            "type" : "long"
          }
        }
      }
    }
'

curl -XGET $1:9200/$2/$3/_mapping?pretty