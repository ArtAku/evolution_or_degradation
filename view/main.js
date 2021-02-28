import { server } from "server";

const port = process.env.PORT || 5000

function main() {
  server.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }    console.log(`server is listening on ${port}`)
  })
}

main();