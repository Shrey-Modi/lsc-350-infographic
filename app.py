import streamlit as st
import matplotlib.pyplot as plt
import squarify
import secrets


def main():
    st.title('LSC Infographic: Global Chip Shortage')

    st.write('Chip Demand by Revenue (in billion $)\n\nsource : https://spectrum.ieee.org/chip-shortage')
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # frozen = st.slider('Change Frozen Volume', 20, 200, 150)
    # values = [350, 220, 170, frozen, 50]
    # labels = ['Liquid\n volume: 350k', 'Savoury\n volume: 220k',
    #         'Sugar\n volume: 170k', f'Frozen\n volume: {frozen}k',
    #         'Non-food\n volume: 50k']

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
                 color=[f"#{secrets.token_hex(3)}" for i in treemap_data], alpha=0.7)
    plt.axis('off')
    st.pyplot()


if __name__ == '__main__':
    main()
