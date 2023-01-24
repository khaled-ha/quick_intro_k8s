import express from 'express'
import os from 'os'

const app = express()
const PORT = 3000

app.get(
    "/", (req, res) => {
        const helloMessage = `Version 2 : Hello frm the ${os.hostname()}`
        console.log(helloMessage)
        res.send(helloMessage)
    }
)


app.listen(PORT ,() => {
    console.log(`Web app is listening at the port ${PORT}`)
})