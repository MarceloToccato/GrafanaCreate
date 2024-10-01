# O código a seguir tem a utilidade de criar um arquivo .json, com intuito de importalo para o grafana
# Fazendo o grafana criar um dashboard já pronto

# Usar template no zabbix 'Qlik Sense - Central Node'

###########################################Criando as variaveis para Do host e do grupo dohost######################################



Hostgroup = ''  # Altere para o grupo de host que seu host se encontra'
Hostname = '' # Altere para o nome do seu Host 



#################################################Criador do Id aleatório###########################################################




# O código a baixo serve para  criar um ID unico para o uid q é definido como f'{code}' no código



import random as rm #Importando a biblioteca random
code = [] #Criando uma array onde a O ID unico ficara



# Todos os caracteres que podem ser utilizados no ID unico
Caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



for i in range (7): #Loop para adicionar os caracteres aleatorios na array code
         
         
            simbolos = rm.choice(Caracteres) #Escolhendo caracter
         
            code.append(simbolos) #Adiciona o caracter na array code


code = (''.join(code)) #Define que code é um texto tudo junto sem espaço entre os itens
#Fazendo com que ele forme um ID unico



#################################################Importando o .json###########################################################



# Essa variável 'grafanajson' é um .json que caso importado cria um dashboard no grafana
# Porém nos lugares onde se coloca o Hostgroup e o Hostname colocamos os seguintes comandos 
# f'{Hostgroup}' e f'{hostname} para importar as variávels já definidas

# caso queira importa seu proprio .json faça os seguintes passos
# altere todos os True,False,None e para true,false,null
# altere o nome do group host e o host para f'{Hostgroup}' e f'{Hostname}
# altere a uid para f'{code}'

grafanajson = {
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": True,
        "hide": True,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": True,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 110,
  "links": [],
  "panels": [
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 0,
        "y": 0
      },
      "id": 40,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Uptime"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Uptime",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bool_on_off"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 3,
        "y": 0
      },
      "id": 39,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Zabbix agent availability"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Agent Zabbix Status",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 6,
        "y": 0
      },
      "id": 57,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "name",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Tokens em quarentena"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Tokens em quarentena",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 9,
        "y": 0
      },
      "id": 59,
      "options": {
        "colorMode": "none",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "none",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Tokens em uso"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "tokens em uso",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 12,
        "y": 0
      },
      "id": 61,
      "options": {
        "colorMode": "none",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "none",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Total de tokens"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "total de tokens",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 15,
        "y": 0
      },
      "id": 58,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "none",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Token Alocados"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Token Alocados",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 18,
        "y": 0
      },
      "id": 60,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "none",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Tokens Disponíveis"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Tokens Disponíveis",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 21,
        "y": 0
      },
      "id": 31,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "C:: Total space"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "espaço total",
      "transparent": True,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 80
              },
              {
                "color": "red",
                "value": 90
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 2
      },
      "id": 5,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "CPU utilization"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "utilização de CPU",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 31,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 80
              },
              {
                "color": "red",
                "value": 90
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 4,
        "y": 2
      },
      "id": 7,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "CPU utilization"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Utilização de CPU",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "fieldMinMax": True,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          },
          "unit": "gbytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "C:: Space utilization"
            },
            "properties": [
              {
                "id": "thresholds",
                "value": {
                  "mode": "percentage",
                  "steps": [
                    {
                      "color": "green",
                      "value": None
                    },
                    {
                      "color": "#EAB839",
                      "value": 80
                    },
                    {
                      "color": "red",
                      "value": 90
                    }
                  ]
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "C:: Used space"
            },
            "properties": [
              {
                "id": "min",
                "value": 0
              },
              {
                "id": "max",
                "value": 119
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 2
      },
      "id": 38,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "C:: Used space"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "C:: Space utilization"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "C",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "espaço utilizado",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds",
            "seriesBy": "last"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 27,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 1,
            "pointSize": 2,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "always",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "fieldMinMax": False,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "green",
                "value": 1
              }
            ]
          },
          "unit": "GBs"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "C:: Total space"
            },
            "properties": [
              {
                "id": "custom.drawStyle",
                "value": "points"
              },
              {
                "id": "color",
                "value": {
                  "fixedColor": "dark-red",
                  "mode": "fixed"
                }
              },
              {
                "id": "max",
                "value": 128849018880
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "C:: Used space"
            },
            "properties": [
              {
                "id": "max",
                "value": 128849018880
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 16,
        "y": 2
      },
      "id": 12,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "C:: Used space"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "C:: Total space"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "espaço utilizado",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Total memory"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#73BF69",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Used memory"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Memória usada"
              },
              {
                "id": "max",
                "value": 34359738368
              },
              {
                "id": "min",
                "value": 0
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "green",
                      "value": None
                    },
                    {
                      "color": "yellow",
                      "value": 26843545600
                    },
                    {
                      "color": "red",
                      "value": 31138512896
                    }
                  ]
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Memory utilization"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "mode": "thresholds"
                }
              },
              {
                "id": "displayName",
                "value": "Memória utilizada"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "percentage",
                  "steps": [
                    {
                      "color": "green",
                      "value": None
                    },
                    {
                      "color": "#EAB839",
                      "value": 80
                    },
                    {
                      "color": "red",
                      "value": 90
                    }
                  ]
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 6
      },
      "id": 15,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Total memory"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "C",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Memory utilization"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Used memory"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 28,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 2,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          },
          "unit": "decgbytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Total memory"
            },
            "properties": [
              {
                "id": "custom.drawStyle",
                "value": "points"
              },
              {
                "id": "color",
                "value": {
                  "fixedColor": "dark-red",
                  "mode": "fixed"
                }
              },
              {
                "id": "max",
                "value": 34359738368
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "green",
                      "value": None
                    },
                    {
                      "color": "#EAB839",
                      "value": 26843545600
                    },
                    {
                      "color": "red",
                      "value": 31138512896
                    }
                  ]
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Used memory"
            },
            "properties": [
              {
                "id": "max",
                "value": 34359738368
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 4,
        "y": 6
      },
      "id": 16,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Used memory"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Total memory"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "memoria utilizada",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": None
              },
              {
                "color": "yellow",
                "value": 10
              },
              {
                "color": "green",
                "value": 20.0001
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 6
      },
      "id": 14,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showThresholdLabels": False,
        "showThresholdMarkers": True,
        "sizing": "auto"
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Free swap space in %"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "swap memory disponível",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 28,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 3,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": None
              },
              {
                "color": "yellow",
                "value": 10
              },
              {
                "color": "green",
                "value": 20
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 16,
        "y": 6
      },
      "id": 17,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Free swap space in %"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "swap memory disponível",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 80
              },
              {
                "color": "red",
                "value": 90
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 10
      },
      "id": 46,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showThresholdLabels": False,
        "showThresholdMarkers": True,
        "sizing": "auto"
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk utilization"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "utilização de disco",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 28,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 80
              },
              {
                "color": "red",
                "value": 90
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 4,
        "y": 10
      },
      "id": 47,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": False
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk utilization"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "utilização de disco",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 30
              },
              {
                "color": "red",
                "value": 40
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 10
      },
      "id": 44,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk average queue size (avgqu-sz)"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Tamanho médio da fila do disco",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 28,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 3,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 30
              },
              {
                "color": "red",
                "value": 40
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 16,
        "y": 10
      },
      "id": 45,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk average queue size (avgqu-sz)"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Tamanho médio da fila do disco",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 380,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 350
              },
              {
                "color": "red",
                "value": 400
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 14
      },
      "id": 18,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Number of processes"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "numero de precessos",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 27,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 350
              },
              {
                "color": "red",
                "value": 400
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 4,
        "y": 14
      },
      "id": 20,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": False
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Number of processes"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "numero de precessos",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 350
              },
              {
                "color": "red",
                "value": 400
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "0 C:: Disk read rate"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Leitura"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "0 C:: Disk write rate"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Grvação"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 14
      },
      "id": 54,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk read rate"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk write rate"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "taxa de leitura/gravação em disco",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "#EAB839",
                "value": 350
              },
              {
                "color": "red",
                "value": 400
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "0 C:: Disk read rate"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Leitura"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "0 C:: Disk write rate"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Grvação"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Grvação"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 16,
        "y": 14
      },
      "id": 62,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk read rate"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "0 C:: Disk write rate"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "taxa de leitura/gravação em disco",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 18
      },
      "id": 56,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Memory pages per second"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Páginas de memória por segundo",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 27,
            "gradientMode": "none",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              },
              {
                "color": "red",
                "value": 1000
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 4,
        "y": 18
      },
      "id": 55,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Memory pages per second"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Páginas de memória por segundo",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "fieldMinMax": True,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits received"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "bits recebido"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits sent"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "bits enviados"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 18
      },
      "id": 52,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": False
        },
        "showPercentChange": False,
        "textMode": "auto",
        "wideLayout": True
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits received"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits sent"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Bits Enviados/Recebidos",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "alexanderzobnin-zabbix-datasource",
        "uid": "bdok9l2ycc6ioc"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "axisBorderShow": False,
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "hidden",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 6,
            "gradientMode": "hue",
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "insertNulls": False,
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": None
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits received"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Bits recebidos"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits sent"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Bits enviados"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 16,
        "y": 18
      },
      "id": 48,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": True
        },
        "tooltip": {
          "maxHeight": 600,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits received"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "A",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        },
        {
          "application": {
            "filter": ""
          },
          "countTriggersBy": "",
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "bdok9l2ycc6ioc"
          },
          "evaltype": "0",
          "functions": [],
          "group": {
            "filter": f'{Hostgroup}'
          },
          "hide": False,
          "host": {
            "filter": f'{Hostname}'
          },
          "item": {
            "filter": "Interface Red Hat VirtIO Ethernet Adapter(Ethernet): Bits sent"
          },
          "itemTag": {
            "filter": ""
          },
          "macro": {
            "filter": ""
          },
          "options": {
            "count": False,
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useTrends": "default",
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "B",
          "resultFormat": "time_series",
          "schema": 12,
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "textFilter": "",
          "trigger": {
            "filter": ""
          }
        }
      ],
      "title": "Bits Enviados/Recebidos",
      "type": "timeseries"
    }
  ],
  "refresh": "10s",
  "schemaVersion": 39,
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timeRangeUpdatedDuringEditOrView": False,
  "timepicker": {},
  "timezone": "browser",
  "title": f'{Hostname}',
  "uid": f'{code}',
  "version": 5,
  "weekStart": ""
}



###############################################Criando arquivo .json e abrindo a pasta json#####################################



# Os códigos seguinte tem o intuito de:
# Salvar a variavel grafanajson em um arquivo .json 
# Abrir o explorador de arquivos onde o tal arquivo se encontra 

import os #   Importa uma biblioteca para conseguir mexer no sistema operacional via python
import json # Importa uma biblioteca para conseguir mexer com json

folder_path = 'json' #Define a pasta onde o arquivo será salvo

file_name = f'{Hostname}'+'.json' #Define o nome que o arquivo terá, juntando o nome do host com o .json


file_path = os.path.join(folder_path, file_name) #cria o caminho onde o arquivo será salvo


with open (file_path,'w') as grafana: #abre um arquivo onde a variavel a cima definiu
  #escreve o conteudo da variável 'grafanajson'
  json.dump(grafanajson, grafana)

  #Caso o arquivo não esteja nesse direcionamente altere para onde a pasta com o código se encontra 
diretorio = 'C:Local\\Do\\GrafanaCreate\\json' #defina o diretório onde o json foi salvo  

os.startfile(diretorio) 
#abre o explorador de arquivos onde o json está. 
#para apenas ter que arrastar o arquivo para a aba de importar do grafana



############################################################################################################
