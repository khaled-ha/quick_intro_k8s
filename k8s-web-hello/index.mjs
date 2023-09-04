import express from 'express'
import os from 'os'

const app = express()
const PORT = 3000

app.get(
    "/", (req, res) => {
        const helloMessage = 'Message : Hello k8s trainer '
        console.log(helloMessage)
        res.send(helloMessage)
    }
)

app.get(
    "/fastapi", (req, res) => {
        const helloMessage = 'Welcome to express from fastapi request'
        console.log(helloMessage)
        res.send(helloMessage)
    }
)


app.listen(PORT ,() => {
    console.log(`Web app is listening at the port ${PORT}`)
})