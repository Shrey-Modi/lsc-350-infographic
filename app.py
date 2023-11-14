import streamlit as st
import matplotlib.pyplot as plt
import squarify
import secrets
import pandas as pd


def main():
    st.title('LSC Infographic: Global Chip Shortage')

    # Heading
    st.header('What is a Chip?')

    # add image with text beside it microchip.png
    col2, col1 = st.columns([2,1])
    col1.image('microchip.png')
    col2.write('A microchip (also known as a chip, a computer chip, an integrated circuit or IC) is a compact flat piece of silicon that contains a collection of electrical circuits. Transistors on a chip function as microscopic electrical switches that can turn a current on or off. On the silicon wafer, the pattern of small switches is formed by adding and removing materials to produce a multilayered latticework of linked structures. Microchips are printed on silicon wafers, which are made from silica sand. Microchips are found in nearly every electronic gadget we own today, including cellphones, gaming consoles, automobiles, and medical equipment.')

    st.header('Why are they important?')
#     Processing Power:
# Chips are the basic components of electronic devices, providing the processing power required for computers, smartphones, tablets, and other computing devices.
# Digital Storage:
# Chips are required for digital memory, data storage and retrieval in electronic devices.
# Communication and Connectivity:
# They provide power to networking components like routers and modems, as well as wireless communication technologies like Wi-Fi, Bluetooth, and cellular networks.
# Electronics for the Home:
# Semiconductors are used in almost all current consumer electronics, including televisions, cameras, audio devices, and game consoles.
# Vehicle Applications:
# Chips help with navigation, operate engine management systems, enable safety features like airbags and anti-lock brakes, and contribute to the functioning of entertainment systems.
# Research and development:
# Chips are vital in scientific research, simulations, and data processing.

# add each of these in columns and images beside them
    col1, col2 = st.columns([1,2])
    col1.image('processing.jpeg')
    col2.header('Processing Power')
    col2.write('Chips are the basic components of electronic devices, providing the processing power required for computers, smartphones, tablets, and other computing devices.')

    col1, col2 = st.columns([2,1])
    col2.image('storage.png')
    col1.header('Digital Storage')
    col1.write('Chips are required for digital memory, data storage and retrieval in electronic devices.')

    col1, col2 = st.columns([1,2])
    col1.image('communication.png')
    col2.header('Communication and Connectivity')
    col2.write('They provide power to networking components like routers and modems, as well as wireless communication technologies like Wi-Fi, Bluetooth, and cellular networks.')

    col1, col2 = st.columns([2,1])
    col2.image('home.png')
    col1.header('Electronics for the Home')
    col1.write('Semiconductors are used in almost all current consumer electronics, including televisions, cameras, audio devices, and game consoles.')


    col1, col2 = st.columns([2,3])

    col1.image('vehicle.png')
    
    col2.header('Vehicle Applications')
    col2.write('Chips help with navigation, operate engine management systems, enable safety features like airbags and anti-lock brakes, and contribute to the functioning of entertainment systems.')


    st.header('Chip Demand by Revenue (in billion $)')
    
    st.set_option('deprecation.showPyplotGlobalUse', False)


    treemap_data = {
        'Automotive': 39.5,
        'Consumer': 60.1,
        'Wireless': 126.7,
        'Computing': 160.2,
        'Communication': 36.3,
        'Industrial': 41.6
    }
    color_list = ['#3F1973', '#3407A0', '#9C9FD9',
                '#402A01', '#BBA26A', '#D6B798']

    plt.rc('font', size=8)
    squarify.plot(sizes=treemap_data.values() , label=[f"{k}\n{v}" for k, v in treemap_data.items()],
                color=color_list,#[f"#{secrets.token_hex(3)}" for i in treemap_data],
                alpha=0.7)
    plt.axis('off')
    st.pyplot()
    st.write('source : https://spectrum.ieee.org/chip-shortage')


    st.markdown('---')
    st.title('Causes of Shortage of Chips on a global level')
    st.header('Increased Electronics Demand')
    st.write("As more people worked, studied, and enjoyed themselves at home due to the COVID-19 epidemic, demand for electronic equipment increased. This raised demand for laptops, tablets, and gaming consoles, putting pressure on the semiconductor supply chain.")
    internet_data = pd.read_csv('internet.csv')
    countries = st.multiselect(
            "Choose countries", internet_data['Entity'].unique(), ["United States"]
        )
    
    for country in countries:
        internet_data[country] = internet_data[internet_data['Entity'] == country]['Internet Users(%)']
    internet_start_year = st.slider('start year', 2000, 2020, 2000)
    internet_data['Year'] = internet_data['Year'].astype(str)
    # internet_data = internet_data[internet_data['Entity'].isin(countries)]
    # merge rows
    internet_data = internet_data[['Year'] + countries]
    # rename country columns
    internet_data = internet_data.groupby(['Year']).sum().reset_index()
    internet_data = internet_data[internet_data['Year'].astype(int) >= internet_start_year]
    st.line_chart(internet_data, x='Year', y=countries)
    st.write('source: https://www.kaggle.com/datasets/ashishraut64/internet-users/')

    st.header('Impact on the Automotive Industry')
    st.write("The automobile industry, a major user of semiconductors, was impacted. Because of the pandemic's unpredictability, several automakers cut chip orders. When demand recovered, semiconductor makers were unable to keep up with the unexpected rise.")
    data = pd.read_csv('DAUPSA.csv')

    data['month'] = data['DATE'].apply(lambda x: x[:7])
    start_year = st.slider('start year', 2005, 2021, 2010)
    data = data[data['DATE'].apply(lambda x: int(x[:4]) >= start_year)]

    data['Domestic auto production'] = data['DAUPSA'].astype(float)
    st.line_chart(data, x='month', y='Domestic auto production') 
    st.write("Domestic auto production is defined as all autos assembled in the U.S.\n\nSource: https://fred.stlouisfed.org/series/DAUPSA")

    st.header("Disruptions in the Supply Chain")
    st.write("The epidemic affected worldwide supply lines, hurting semiconductor manufacture and delivery. Manufacturing facility lockdowns, limitations, and closures hampered or temporarily halted output.")
    # shipping_data = pd.read_csv('shipping.csv')
    cases = pd.read_csv('cases_clean.csv')

    cases_start_year = st.slider('number of months to include', 1, 35, 12)
    st.line_chart(cases.tail(cases_start_year), x='month', y='cumulative_confirmed')

    st.markdown('---')

    st.title('Impact of Chip Shortage')
    
    st.header('Disruptions in the Automotive Industry')
    st.write("Due to a lack of semiconductor chips, automakers have experienced severe production delays and, in some cases, temporary shutdowns. This has resulted in lower car stocks, longer lead times, and, as a result, higher costs for some models.")

    st.header('Consumer Effect')
    st.write("Consumers may experience lengthier wait periods for electrical devices and cars, as well as price increases in some situations, as a result of the supply-demand imbalance. Limited product options and delayed product introductions might have an influence on the entire consumer experience.")

    st.header('Job losses and their economic consequences')
    st.write("Due to manufacturing slowdowns or temporary shutdowns, industries strongly reliant on semiconductor manufacture, such as automotive, may face employment losses. The economic impact goes beyond the semiconductor industry and affects associated industries as well as the entire economy.")

    st.header('Electronics Manufacturing Difficulties')
    st.write("The shortfall has hampered the manufacture of a wide range of electronic goods, including cellphones, laptop computers, game consoles, and household appliances. As a result, customers must wait longer and producers may suffer financial losses.")

    st.header('Disruptions in the Supply Chain')
    st.write("The chip scarcity has revealed flaws in global supply systems, leading businesses to rethink and diversify their supply sources. Increased supply chain risk awareness may lead to more robust and diverse supply chain strategies in the future.")

if __name__ == '__main__':
    main()
