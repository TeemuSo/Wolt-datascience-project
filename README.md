# Data Science Summer Intern assignment 2021 Sormunen Teemu

![](imgs/wolt_demo_project_short.gif)

# Project overview

This project is intended to be used as visualization and prediction tool, to be used either by the end-user, the courier, or the management team. This project is not a showcase of good coding practises or beautiful and fail-proof user interface. This project is more of a proof-of-concept where I have analysed the data, decided on what would be interesting, and coded it in fairly short time. This is to show the ability to take on new challenges quickly and efficiently. 

## The problem

First choice every Wolt courier has to make in the morning, is to choose the area he decides to operate within. Every courier wants to maximize their efficiency, and Wolt most likely also wants to maximize the efficiency of its couriers. It can be hard to predict where and when the courier should be to maximize the daily amount of deliveries.

## The solution

This project provides small proof-of-concept for monitoring the amount of orders during the day. In this project, customizable heatmap is made to indicate in which areas the restaurants are busy. This type of solution provides historical information about deliveries which can then be applied to predict amount of orders on hourly, daily, or even monthly level when enough data is provided. 

User is able to choose the interval between which to investigate the heatmap distribution via small interface as seen below.

![](imgs/user_panel.png)


Single companies shouldn't be identifiable from this map due to data privancy conserns. The heatmap can be made more general by increasing the pointsize, making the individual datapoints to vanish as can be seen below. From this graph we can see the areas where orders are placed as heat, but not single individual companies.

![](imgs/vanished_datapoints.png)


The tool also allows user to get broader overview of the data by choosing to start animation. Animation is useful for visualizing how daily demand happens. User can view what areas are busy during certain time periods within day, or within a month. Before starting the animation, user has to configure the animation parameters. In these parameters *step_size* defines how many samples do we want to jump forward after each iteration, and *sliding_window_size* defines how large portion of the data we want to visualized during each iteration. These parameters can also be seen below.

![](imgs/parameter_selection.png)



Here's one more example of interacting with the user interface.

![](imgs/wolt_demo_project_long.gif)


## Benefits of the solution

This solution can help Wolt scale to larger cities, where demand is even further volatile depending on time of the day. It can be used as high-level tool for planning areas where to expand, or then it could be directly implemented to the application in some form. This way the end-user also would be informed when the restaurants are exceptionally busy. 


## Future work

This work can be extended to provide better predictive capabilities. Bayesian principles could be used to predict the amount of orders that are placed for each company separately. This approach provides us with nicely interpretable probabilistic distributions for predicting the amount of orders placed. This heatmap is most likely generated by producing two-dimensional Gaussian distribution from the densities of single locations. In the predictive model our response variable would consist for each timestep the predictions of the locations that will get orders. The response variable would then be *NxM* matrix, where *N* is timestep, and *M* is predicted location. Our input variables would be all of the features in the dataset.

There's also many other interesting cases where this kind of predictive modelling could be used, but they couldn't be included in this project to keep the scope limited.


# Running the project

To run the project you must create generate Google Map's Javascript API key. This key then has to be inserted either to file called *apikey.txt*, or then user can edit the wolt_data_analysis.ipynb and set the API key directly there.

Dependencies can be installed with
`pip install -r requirements.txt`

Project must be run with Jupyter Notebook.
