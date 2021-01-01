import requests
import bs4
import os
import sys
import json
import csv


class Varibles:
    def __init__(self, url, agent, http, htmlTags:list, htmlAtributs:list, htmlAtributsValues:list, names:list):
        self.url = url
        self.agent = agent
        self.http = http
        self.htmlTags = htmlTags
        self.htmlAtributs = htmlAtributs
        self.names = names
        self.htmlAtributsValues = htmlAtributsValues
        self.deletedChars = {
            '<', '>', '/', '|', '', '*', '!', '?', ',', '.', '=', ':', ';', '{', '}', '&', '^', '#', '~', '(', ')', '_',
            '-', '+'
        }
        self.data = []


class Parser(Varibles):
    def createSoup(self):
        soup = bs4.BeautifulSoup(self.http, 'html.parser')
        rootDiv = soup.findAll(f'{self.htmlTags[0]}', {f'{self.htmlAtributs[0]}': f'{self.htmlAtributsValues[0]}'})
        for el in range(len(self.names)):
            for i in rootDiv:
                localDict = {
                    f'{self.names[el]}': i.findAll(f'{self.htmlTags[el+1]}',
                    {f'{self.htmlAtributs[el+1]}': f'{self.htmlAtributsValues[el+1]}'})
                }
                self.data.append(localDict.get(f'{self.names[el]}'))

        return self.data
    def ReturnParsingData(self):
        data = self.createSoup()
        return data
