# thesis
```python
# Copy /thesis to project directory
# Copy filesInProjectFolder/bin and /py to project directory
# Copy filesInProjectFolder/templates/virtualbox_out in project directory /templates
# Copy filesInProjectFolder/apps to project directory
# Set cronjob as specified in boincdocker.cronjob
# Modify apache2.conf - add remote directory (example in boincdocker.httpd.conf)
# In your config.xml - add validator, assimilator, agregator (example in config.xml)
# Add plan_class_spec.xml in project folder
# Modify project.xml to include virtualbox app
 
# Properly add virtualbox as an app for all platforms

# Modify makeIterationTemplate.py to set url to your remote url
# Modify db_deleteUnsentJobs to set db_name, username and password

# Stage input files:
python stageInputFiles.py

# Use restartLearning.py to start learning from 1, N is number of wus to make initially
python restartLearning.py N
