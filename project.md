---
layout     : default
---

# Final Project Information

The final project for this course is an end-to-edn machine learning project. You will need to propose a topic, acquire or construct a non-trivial dataset, perform a novel analysis of that dataset towards using machine learning to answer a specific question, and finally train an algorithm or series of algorithms to solve the proposed problem. Your final project should contain at minimum the following:

* A clearly formulated, nontrivial description of the problem you are trying to solve. 
* A plan for acquiring the necessary data.  This may take up more of the project than you exact, and I can work with you on acquiring data sets through web scrapping, or requesting access to university resources. 
* An exploratory analysis of your data that clearly summarizes the most relevant aspects, including variable types, variable distributions, label types and distributions, expected patterns and whether they occur, variance and covariance between your variables and labels. This analysis should directly explain your choices of machine learning algorithms.
* You should canvas at minimum two types of algorithms and a reasonably wide space of hyperparameteres for each. You should report your results even if negative for comparison.
* After comparing the models you've chosen above (perhaps in several iterations) you should quire and prepare a sufficient amount of data and do a long train of the most promising algorithm. Your goal is to push your test accuracy (or inverse loss) as high as possible. Pay attention to your loss functions, your training data, and record the choices you make. 

For some projects the steps above will take difference amounts of time. For example, if you need to construct a new dataset (see Providence Lead below) data acquisition may be a large part of your project. However, if you're training large computationally intensive neural networks (see MRI Segmentation below) the dataset model selection, comparison and training will take the bulk of your time. Remember, you need to do something new, you cant just copy a Kaggle kernel. In addition, these are 6-8 week projects, you _cannot_ do them in two week projects and get an A. 


### Final Project Resources:

* [Project Information](https://github.com/tipthederiver/Math-7243-2020/raw/master/Projects/Project%20Information.docx)
* [Project Rubric](https://github.com/tipthederiver/Math-7243-2020/raw/master/Projects/Project%20Rubric.docx)
* [Self Evaluation](https://github.com/tipthederiver/Math-7243-2020/raw/master/Projects/Self%20Evaluation.docx)
* [Group Evaluation](https://github.com/tipthederiver/Math-7243-2020/raw/master/Projects/Group%20Evaluation.docx)

# 2020 Project Gallery

<div class="row">
  {% for project in site.data.projects.projects %}
  <div class="column">
    <div class="card">
      <img src="{{project.thumb-url}}" style="width:100%">
      <div class="container">
        <h4><b>{{project.title}}</b></h4>
        <p>{{project.names}}</p>
        <p><a href="{{project.paper-url}}">Paper</a> | <a href="{{project.pres-url}}">Presentation</a> | <a href="{{project.slide-url}}">Slides</a></p>
      </div>
    </div>
  </div>
  {% endfor %}
</div>
