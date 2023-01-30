const form = document.querySelector("form")
const file = document.querySelector("input")
const reader = new FileReader()

form.addEventListener("submit", async (e) => {
    e.preventDefault()
    
    reader.readAsText(file.files[0]);
    reader.onload = function () {
    
    const document = reader.result
    
    let start = 0

    let end = 81

    const array = []

    for(i = 0; i < 21; i++){
        let string = document.slice(start, end)

        if(i === 0){
            array.push(string.slice(0, 80))
        }
        else{
            array.push(string.slice(1,81))
        }

        start = end

        end = end + 82

    }

    console.log(array)
    
    const object = {data: array}

    const response = fetch("http://127.0.0.1:8000/api/operations/", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: object
    }).then(res => res.json())
    .then(res => res)
    
    console.log(response)
};
})
 