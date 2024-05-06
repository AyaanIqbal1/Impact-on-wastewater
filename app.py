import streamlit as st
import matplotlib.pyplot as plt

# Set page title and favicon
st.set_page_config(page_title="Wastewater Discharges Impact", page_icon=":droplet:")

# Sidebar navigation
sidebar_options = ["Introduction", "Agricultural Wastewater", "Urban Wastewater", "Industrial Wastewater", "Random Forest Regression"]
selected_option = st.sidebar.selectbox("Select a section", sidebar_options)

# Main content
if selected_option == "Introduction":
    st.title("Wastewater Discharges Impact on Environment")
    st.write("This app explores the impact of different types of wastewater discharges on the environment.")

    # Display the title image
    title_image = plt.figure(figsize=(10, 2))
    plt.imshow(plt.imread(r"C:\Users\ayaan\OneDrive\Pictures\word\picture1.png"))
    plt.axis('off')
    st.pyplot(title_image)

elif selected_option == "Agricultural Wastewater":
    st.header("Agricultural Wastewater Discharge's Impact")

    # Sidebar for selecting impact on sea or inland waters
    impact_options = ["Impact on Sea", "Impact on Inland Waters"]
    selected_impact = st.sidebar.radio("Select impact", impact_options)

    if selected_impact == "Impact on Sea":
        st.subheader("Impact on Sea")
        st.write("""
        As per correlation matrix, the correlation was found between
        agricultural wastewater discharges and total discharges to the sea.
        Hence, the regression visualisation indicates this correlation. The
        positive slope suggests that as the discharge of the volume of
        agricultural wastewater increases, the total discharges to the sea
        increases respectively.

        Applied progression formula (Agricultural Wastewater Discharges = 0.1682
        × Total Discharges to the Sea (million m³) + 25.2254) indicates that for
        every additional million cubic meters of agricultural wastewater
        discharges, it increases total discharge to the sea by an average of
        0.1682 (million m³).

        The visualization provides a scatter plot of the actual data points
        (blue) and the predicted regression line (red). The shaded area
        represents the 95% confidence interval for the regression predictions,
        providing a range where we expect the actual value to lie with 95%
        confidence (figure 14).
        """)

        # Figure 14 image path
        figure_14_path = r"C:\Users\ayaan\OneDrive\Pictures\word\picture1.png"
        # Display Figure 14
        fig_14 = plt.figure(figsize=(8, 6))
        plt.imshow(plt.imread(figure_14_path))
        plt.axis('off')
        plt.title('Figure 14')
        st.pyplot(fig_14)

        st.write("""
        The model's coefficient of determination suggests that approximately
        38.82% of the variability in agricultural wastewater discharges can be
        explained by the total discharges to the sea. The confidence intervals
        are relatively tight around the regression line, indicating a certain
        degree of precision in the model's predictions.
        """)

    elif selected_impact == "Impact on Inland Waters":
        st.subheader("Impact on Inland Waters")
        st.write("""
        Opposite to the impact on the sea, it was found a negative corelation to
        between agricultural wastewater discharges and total discharges to the
        inland waters. This implies that an increase in inland discharges is
        associated with a slight decrease in agricultural wastewater discharges.
        This relationship could be influenced by various factors, including the
        management practices for agricultural and industrial wastewater or the
        geographical distribution of agricultural areas relative to inland water
        bodies.

        Applied progression formula: Agricultural wastewater discharges =
        −0.01035 × Total discharges to Inland waters (million m³) + 130.1775
        Agricultural wastewater discharges = −0.01035 × Total discharges to
        Inland waters (million m³) + 130.1775 indicates that for every million
        cubic meters increase in inland discharges, the volume of agricultural
        wastewater discharges decreases by approximately 0.01035 million cubic
        meters.

        These models quantify the association between the total discharges and
        agricultural wastewater discharges, with positive association for sea
        discharges and a slight negative association for inland discharges
        (figure 15)
        """)

        # Figure 15 image path
        figure_15_path = r"C:\Users\ayaan\OneDrive\Pictures\word\picture2.png"
        # Display Figure 15
        fig_15 = plt.figure(figsize=(6, 8))
        plt.imshow(plt.imread(figure_15_path))
        plt.axis('off')
        plt.title('Figure 15')
        st.pyplot(fig_15)

elif selected_option == "Urban Wastewater":
    st.header("Urban Wastewater Discharge's Impact on Sea")
    st.write("""
    Applied progression model (Urban Wastewater Discharges = 0.03337 × Total
    Discharges to the Sea (million m³) + 74.2727) suggests that for every
    million cubic meters increase urban wastewater discharges, the volume of
    total discharges to sea increases by approximately 0.03337 million cubic
    meters.

    The coefficient of determination, R², for this regression is
    approximately 0.2462, which indicates that around 24.62% of the
    variability in urban wastewater discharges can be explained by the total
    discharge to the sea. It\'s a modest fit, indicating that while there is
    some relationship, a significant portion of the variability is not
    captured by this model, and another factor may be influencing urban
    wastewater discharges (figure 16).
    """)

    # Figure 16 image path
    figure_16_path = r"C:\Users\ayaan\OneDrive\Pictures\word\picture3.png"
    # Display Figure 16
    fig_16 = plt.figure(figsize=(8, 6))
    plt.imshow(plt.imread(figure_16_path))
    plt.axis('off')
    plt.title('Figure 16')
    st.pyplot(fig_16)

elif selected_option == "Industrial Wastewater":
    st.header("Industrial Wastewater Discharge's Impact on Inland Waters")
    st.write("""
    The regression analysis demonstrates a positive relationship between the
    volume of industrial wastewater discharges and the volume of inland
    water discharges. The model's moderate R² value indicates a substantial
    association, yet it also suggests that other factors play a role in
    determining industrial wastewater discharges that the model does not
    capture.

    Applied progression formula: Industrial Wastewater Discharges = 0.2957 ×
    Total Discharges to Inland Waters (million m³) − 79.3546 where
    coefficient 0.2957 suggests that for each million cubic meters increase
    in the industrial wastewater discharges, inland water discharges
    increase by approximately 0.2957 million cubic meters. The R² value is
    0.4916, indicating that about 49.16% of the variability in industrial
    wastewater discharges is explained by the model, showing a moderate fit
    (figure 17).
    """)

    # Figure 17 image path
    figure_17_path = r"C:\Users\ayaan\OneDrive\Pictures\word\picture4.png"
    # Display Figure 17
    fig_17 = plt.figure(figsize=(10, 6))
    plt.imshow(plt.imread(figure_17_path))
    plt.axis('off')
    plt.title('Figure 17')
    st.pyplot(fig_17)

elif selected_option == "Random Forest Regression":
    st.header("Random Forest Regression Analysis")
    st.write("""
    The Random Forest regression model was used to predict deaths due to
    unsafe WASH practices, based on various environmental and
    infrastructural predictors. This evaluation typically includes metrics
    such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean
    Absolute Error (MAE), and R-squared (R^2) to gauge how well the model
    predicts continuous numerical outcomes. Here are the key outcomes were
    calculated:

    -   Mean Squared Error (MSE): The model achieved an MSE of approximately
        0.014. While the MSE is lower than what we observed with the linear
        regression model, it still represents the average of the squares of
        the errors---the difference between the observed values and the
        values predicted by the model.

    -   R-squared (R²): The R² value is approximately -10.72. Like the
        linear regression model, a negative R² value indicates that the
        model does not fit the data well and performs worse than a simple
        mean-based model.

    The visualization (figure 18) of feature importance from the Random
    Forest model reveals which predictors have the most influence on
    predicting deaths due to unsafe WASH practices. The importance values
    help identify which environmental and infrastructural features
    contribute most to the model\'s predictions.
    """)

    # Figure 18 image path
    figure_18_path = r"C:\Users\ayaan\OneDrive\Pictures\word\picture5.png"
    # Display Figure 18
    fig_18 = plt.figure(figsize=(8, 4))
    plt.imshow(plt.imread(figure_18_path))
    plt.axis('off')
    plt.title('Figure 18')
    st.pyplot(fig_18)

    st.write("""
    However, the negative R² value suggests that the Random Forest model,
    despite its ability to capture non-linear relationships and interactions
    between predictors, still does not perform well on this dataset. This
    could be due to underlying complexities in the data that are not
    captured by the current set of predictors or due to overfitting to the
    training data. Moreover, the model\'s poor performance suggests caution
    in interpreting these importance values as definitive indicators of
    causal relationships.

    Therefore, linear and Random Forest regression analyses struggled to
    accurately predict deaths due to unsafe WASH practices based on the
    selected predictors. This highlights the complexity of the relationship
    between WASH practices and health outcomes, which may be influenced by a
    wide range of socioeconomic, environmental, and behavioural factors not
    fully captured in the current dataset (figure 19).
    """)

    # Figure 19 image path
    figure_19_path = r"C:\Users\ayaan\OneDrive\Pictures\word\picture6.png"
    # Display Figure 19
    fig_19 = plt.figure(figsize=(6, 4))
    plt.imshow(plt.imread(figure_19_path))
    plt.axis('off')
    plt.title('Figure 19')
    st.pyplot(fig_19)