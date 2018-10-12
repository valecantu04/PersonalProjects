from django.db.models import Count, Max, Min, Avg
from .fusioncharts import FusionCharts
from .models import *

def graph1():
    #dataSource is the core of how the chart is made and formated
    dataSource = {}
    #setting chart values/parameters
    #we're keeping all the graph styles the same, so only change caption, [x/y]AxisName
    dataSource['chart'] = { 
      "caption" : "GPA for Program and Cohort Year",
      "xAxisName": "Program by Year",
      "yAxisName": "Average GPA",
        "paletteColors" : "#ffcd00",
        "bgColor" : "#ffffff",
        "exportenabled": "1",
        "exportatclient": "1",
        "exporthandler": "http://export.api3.fusioncharts.com",
        "html5exporthandler": "http://export.api3.fusioncharts.com",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "showXAxisLine": "1",
        "xAxisLineColor" : "#999999",
        "showValues" : "0",
        "divlineColor" : "#999999",
        "divLineIsDashed" : "1",
        "showAlternateHGridColor" : "0",
        "theme": "ocean"
    }
    #here we are gathering the data from the database
    cohortYearProgramNameAvgGPA = Student.objects.values('programname', 'cohortyear').order_by('programname', 'cohortyear').annotate(Avg('currentoverallgpa'))
    #key: data, value: a VERY specific dictionary of values
    dataSource['data'] = []
    #each bar in the graph follows a specific dictionary format
    #the label, value can be chosen from the query
    for el in cohortYearProgramNameAvgGPA:
        data = {}
        data['label'] = '{0} {1}'.format(el['programname'], el['cohortyear'])
        data['value'] = el['currentoverallgpa__avg']
        dataSource['data'].append(data)
    #return the FusionChart object
    return FusionCharts("column2D", "ex1", "500", "400", "chart-1", "json", dataSource)
   

def graph2():
    '''
    Graphing the number of students in each program for each year.
    '''
    # Datasource is how the chart is made and formatted
    dataSource = {}
    # How the chart is styled. Same style as the above chart.
    dataSource['chart'] = {
    "caption" : "Program Activity by Year",
    "xAxisName": "Program and Cohort Year",
    "yAxisName": "Number of Participants",
        "paletteColors" : "#ffcd00",
        "bgColor" : "#ffffff",
        "exportenabled": "1",
        "exportatclient": "1",
        "exporthandler": "http://export.api3.fusioncharts.com",
        "html5exporthandler": "http://export.api3.fusioncharts.com",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "showXAxisLine": "1",
        "xAxisLineColor" : "#999999",
        "showValues" : "0",
        "divlineColor" : "#999999",
        "divLineIsDashed" : "1",
        "showAlternateHGridColor" : "0",
        "theme": "ocean"
    }
    # fetches the data to be displayed from the database. Here the program name & cohort year are chosen for the X axis
    # and the Count of the students in each is stored as the Y axis 
    cohortYearProgramNameNumberStudents = Student.objects.values('programname', 'cohortyear').order_by('programname', 'cohortyear').annotate(Count('studentid'))
    # In datasource, the key is data, the values are from a dictionary made in the follwing for loop
    dataSource['data'] = []
    # each bar in the graph is made from the dictionary in this format
    for el in cohortYearProgramNameNumberStudents:
        data = {}
        data['label'] = '{0} {1}'.format(el['programname'], el['cohortyear']) # the label is chosen from the query
        data['value'] = el['studentid__count'] # the value of the Y axis of the bar
        dataSource['data'].append(data)
    # return the FusionChart object
    return FusionCharts("column2D", "ex3", "700", "400", "chart-2", "json", dataSource)
        