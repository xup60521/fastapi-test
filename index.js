

const input = document.getElementById("input")
const submit = document.getElementById("submit")
const list = document.getElementById("list")
const url = "https://fastapi-test-nine.vercel.app"
// const url = "http://127.0.0.1:8000"

submit.addEventListener("click", async ()=>{

    const text = input?.value
    if (text) {
        const formdata = new FormData()
        formdata.append("name", text)
        fetch(`${url}/post` , {
            "method": "POST",
            body: formdata,
        }).then(()=>window.location.reload())
    }
    
})

window.addEventListener("load", async ()=>{
    fetch(`${url}/post`).then(res=>res.json()).then((res)=>{
        res.map(item=>{
            const btn = document.createElement("button")
            const div = document.createElement("div")
            div.id = "item"
            const span = document.createElement("span")
            span.textContent = item.name
            div.appendChild(span)
            btn.textContent = "delete"
            btn.addEventListener("click", async () => {
                fetch(`${url}/post/${item["_id"]}`).then(()=>window.location.reload())
            })
            div.appendChild(btn)
            list.appendChild(div)
        })
    })
})