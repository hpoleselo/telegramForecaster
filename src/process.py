import pandas as pd
import forecast


def processData(period, wind_speed, wind_direction, wave_height, wave_direction, energy, dates, time):
    """ All the data retrieved is gonna be treated now to be sent to Telegram
    Send as text? Generate table using Pandas but then converting to csv style?
    """

    initialColumns = checaDeslocamento(time)

    # Creating our pandas dataframe
    forecastTable = {}
    columns = []
    counter = 0
    # 8 is the number of subdivisions in a day
    secondThreshold = initialColumns + 8
    thirdThreshold = secondThreshold + 8
    #fourthThreshold = 

    index = ['Horário','Período da Ondulação:','Velocidade do Vento:','Direção do Vento:', 'Tamanho da Ondulação:','Direção da Ondulação:', 'Energia da Ondulação:']
    
    # Colocar len
    for i in range(23):
        counter+=1
        if counter <= initialColumns:
            columns.append(dates[0])   
        elif counter <= secondThreshold:
            columns.append(dates[1])
        elif counter <= thirdThreshold:
            columns.append(dates[2])
        elif counter > thirdThreshold:
            columns.append(dates[3])


    df = pd.DataFrame(forecastTable, columns=columns, index=index)
    print(df)
    # pegar max.energy() p/ avaliar melhor dia com min.wind()
    # Using pandas, try to create a table from this csv and then generate image/text?


def generateImage(df):
    pass
    #return image


def checaDeslocamento(time):
    """ Since the day the we're looking isn't going to display the full day (all the eight times), then we have to know before how many
    days we're going to plot since it's not 8. We do that by checking the transition between PM -> AM (when it's the transition between days) 
    
    The variable returned here is the number of columns with the first day to be plotted.
    """
    pmCounter = 0
    amCounter = 0
    generalCounter = 0
    initialTime = time[0]
    initialState = initialTime[-2:]
    for i in range(len(time)):
        generalCounter += 1
        currentTime = time[i]
        # Since we want to detect the transition from PM to AM, then we just have to check when this transiion happens.
        # -2: gets the PM/AM suffix from the time
        currentState = currentTime[-2:]

        if currentState == "AM":
            amCounter += 1

        if not (currentState == initialState):
            print("Geral: Houve transição de horário!")
            if (initialState == "PM"):
                print("\nCaso o estado seja PM:")
                print("Fez a transicao de dias!")
                print("Plotar: ", generalCounter-1)
            else:
                print("\nCaso o estado seja AM:")
                print("Não houve transição de dias")
                print("Plotar horarios pela manhã: ", amCounter)
                print("Plotar horarios PM: 4")
            break

    # Since we detect the transition after n+1 iterations, we have to decrease by 1
    displacement = generalCounter - 1

    """
    if (pmCounter < amCounter):
        print("Quer dizer que a transicao foi ..")
    """

    return displacement

def main():
    response = forecast.checkPage()
    pageText = forecast.checkContent(response)
    period, wind_speed, wind_direction, wave_height, wave_direction, energy, dates, time = forecast.getContent(pageText)
    processData(period, wind_speed, wind_direction, wave_height, wave_direction, energy, dates, time)


if __name__ == "__main__":
        main()
