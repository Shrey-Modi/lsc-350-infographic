import streamlit as st
import matplotlib.pyplot as plt
import squarify

def main():
    st.title('LSC Infographic: Global Chip Shortage')

    st.text('test treemap')
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    frozen = st.slider('Change Frozen Volume', 20, 200, 150)
    volume = [350, 220, 170, frozen, 50]
    labels = ['Liquid\n volume: 350k', 'Savoury\n volume: 220k',
            'Sugar\n volume: 170k', f'Frozen\n volume: {frozen}k',
            'Non-food\n volume: 50k']
    color_list = ['#0f7216', '#b2790c', '#ffe9a3',
                '#f9d4d4', '#d35158', '#ea3033']

    plt.rc('font', size=14)
    squarify.plot(sizes=volume, label=labels,
                color=color_list, alpha=0.7)
    plt.axis('off')
    st.pyplot()


if __name__ == '__main__':
    main()
