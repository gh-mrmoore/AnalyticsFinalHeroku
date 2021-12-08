# Human Trafficking Analysis

## Site
This site will serve as a presentation portal and dashboard to display or link to our results and work as part of our KU Data Analytics and Visualizations Boot Camp. This site will hold our presentation, links to hosted Jupyter notebooks containing our work, an interactive predictive model and other information regarding the presentation.

## Sections

### Home
This section contains:
- The purpose of the project and what this investigation hoped to accomplish.
- An introductory and summary presentation hosted on Google Slides.
- An more detailed background discussing human trafficking, including potential signs of human trafficking.
- A team introduction.
- The communication protocols used during the project.
- A link to the project GitHub repository.

### Data
This section provides an overiew of our data sources, ETL process and database ERD.

### Visualizations
Our visualizations include interactive charts and maps showing:
- Global distribution of cases based on our chosen dataset.
- Annual cases of human trafficking.
- Distribution of victims by age.
- Distribution of victims by type of exploit.
- Distribution of victims by gender.
- Distribution of victims by type of labor.

### Models
Multiple aspects of the dataset were modeled using various machine-learning model types.

#### Exploit Type Modeling
Is is possible to predict the type of exploit given a certain input set? Used a multi-class supervised learning model.

#### Forced Labor Type Modeling
Is it possible to predict the type of forced labor given a certain input set? Used a multi-class supervised learning model.

#### Economic/Demographic Modeling
Is there a relation between certain economic factors and the number of cases in a given country? Used multiple regression to forecast from multiple inputs to a single output. Also attempted to model economic impacts on the number of cases using a deep learning neural network with little success.

#### Regressions
Multiple linear regressions were mapped showing the relationship between case count and various factors separately.

#### Predictive Model
Export of exploit type model as .pkl file that users can interact with via a web-based form.

### Summary
Covering what we learned and where the project could proceed from the point it was left, this section is a quick recap of the project. Several takeaways were noted.