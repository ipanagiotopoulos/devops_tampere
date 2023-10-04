from node:lts-alpine
#setting woring directory
WORKDIR /application_node_js
# all esential files which will be needed for npm install and npm start
ADD /application_node_js/package.json /application_node_js/package-lock.json /application_node_js/
#add all application code to the node.js docker container
ADD /application_node_js/index.js /application_node_js/
#installing all code dependencies
RUN mkdir logs
ADD /logs/service2.log /application_node_js/logs/
RUN npm install
#run the node.js server
CMD [ "npm", "start" ]