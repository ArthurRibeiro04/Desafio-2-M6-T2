const button = document.querySelector("button")
const file = document.querySelector("input")
const reader = new FileReader()

button.addEventListener("click", async (e) => {
    e.preventDefault()
    
    reader.readAsText(file.files[0]);
    reader.onload = async function (e) {
     
    
    const document = reader.result
    

    lines = Math.round(document.length / 81)

    let start = 0

    let end = 81

    const array = []

    for(i = 0; i < lines; i++){
       let string = document.slice(start, end)



        if(i === 0){
            array.push(string.slice(0, 80))
        }
        else if(string === ''){
            
        }
        else{
            array.push(string.slice(1,81))
        }

        start = end

        end = end + 82

        

    }
    
    const object = JSON.stringify({data: array})

    const response = fetch("http://127.0.0.1:8000/api/operations/", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: object
    }).then(res => res.json())
    .then(res => res)
    .catch(err => console.log(err))

    console.log(await response)
    

};
})
 