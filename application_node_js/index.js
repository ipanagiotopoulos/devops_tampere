const express = require('express')
const fs = require('fs')
const env = require('dotenv').config()
const ip = require('ip')


const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

const forward_port = process.env.FORWARD_TO_PORT
const forward_ip = process.env.FORWARD_TO_IP

const port = process.env.port | 8000

if ((!forward_port) || (!forward_ip)) {
  console.log("Application node js failed due to inexistent values FORWARD_PORT and FORWARD_IP")
  process.exit(0);
}

var counter = 1;
var content = ""

const logAndWriteToFile = () => {
  let app_date = new Date()

  if (counter <= 20) {
    console.log("round no:", counter)
    if (counter < 20) {
      content = counter + " " + app_date.toISOString() + " " + forward_ip + ":" + forward_port
    }
    else {
      content = "STOP"
    }
    console.log("msg modify 1", content)
    data = {
      "message": content,
      "name":"Service 1",
      "http_method": "POST"
    }

    fetch("http://" + forward_ip + ":" + forward_port + process.env.POST_ENDPOINT_PATH,
    {
      method: "POST",
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(data)
    })
    .then((response) => {
      if (response.ok) {
        console.log("Request successfully sent\n")
        response.json().then((data) => { console.log(data) })
      }
      else {
        console.log("Request to service 1 failed\n")
      }
    })
    .then(body => {
      if (body)
        console.log(body)
    })
    .catch((error) => {
        console.log("Total failure")
        console.log("Error:", error)
        console.log("msg modify 3", content)
        content = "FAILURE" + " " + error
    })

    fs.appendFile('/application_node_js/logs/service1.log', content + '\n', (err) => {
      if (err) {
        throw(err)
      }
    })
  }
  else {
      console.log("Exiting node.js application code \n Status: 0 ")
      process.exit(0)
  }
  counter++
  setTimeout(logAndWriteToFile, 2000)
  }


app.listen(port, () => {
  console.log(`Server started on port ${port}`)
  logAndWriteToFile()
})