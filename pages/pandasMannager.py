import pandas as pd
import json

def exportToPandas(time, dataList, hasDrag):
    data = []
    for line in range(len(dataList)):
        data.append({})
        data[line]["x"] = dataList[line][0]
        data[line]["y"] = dataList[line][1]
        data[line]["z"] = dataList[line][2]

        data[line]["x velocity"] = dataList[line][3]
        data[line]["y velocity"] = dataList[line][4]
        data[line]["z velocity"] = dataList[line][5]

        data[line]["x acceleration"] = dataList[line][6]
        data[line]["y acceleration"] = dataList[line][7]
        data[line]["z acceleration"] = dataList[line][8]

        if hasDrag:
            data[line]["x without drag"] = dataList[line][9]
            data[line]["y without drag"] = dataList[line][10]
            data[line]["z without drag"] = dataList[line][11]

    dataframes = []

    for datapoint in data:
        dataframes.append(pd.DataFrame(datapoint,index= time))

    return dataframes

def saveIntoExcel(dfListToSave, name):
    writer = pd.ExcelWriter(f"excel saves/{name}.xlsx") # pylint: disable=abstract-class-instantiated

    for i in range(len(dfListToSave)):
        dfListToSave[i].to_excel(writer, sheet_name=f'Throw{i}')

    writer.save()

def saveIntoJSON(name : str ,dfListToSave : pd.DataFrame, **config):
    toSave = [{}]
    for key, value in config.items():
        toSave[0][key] = value
    
    for df in dfListToSave:
        toSave.append(df.to_json())

    print(toSave)
    with open(f'saves/{name}.json','w') as file:
        json.dump(toSave, file)

def loadFromJSON(path):
    with open(f'saves/{path}.json','r') as file:
        stuff = json.load(file)

        dflist = []

        for i in range(1, len(stuff)):
            df = pd.read_json(stuff[i])
            df.index = df.index.strftime('%-S.%f')
            dflist.append(df)

    return dflist, stuff[0]
