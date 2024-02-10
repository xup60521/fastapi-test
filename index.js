

const input = document.getElementById("input")
const submit = document.getElementById("submit")
const list = document.getElementById("list")
const url = "http://fastapi-test-nine.vercel.app"
// const url = "http://127.0.0.1:8000"

submit.addEventListener("click", async ()=>{

    const text = input?.value
    if (text) {
        const formdata = new FormData()
        formdata.append("name", text)
        axios({
            "method": "POST",
            "url": `${url}/post`,
            data: formdata,
            headers: { "Content-Type": "multipart/form-data" },
        }).then(()=>window.location.reload())
    }
    
})

window.addEventListener("load", async ()=>{
    axios.get(`${url}/post`).then((res)=>{
        const regex = /ObjectId/g
        const regex2 = /[()]/g
        const regex3 = /'/g
        const parsed = JSON.parse(res.data.replace(regex, "").replace(regex2, "").replace(regex3, `"`))
        console.log(parsed)
        parsed.map(item=>{
            const btn = document.createElement("button")
            const div = document.createElement("div")
            div.id = "item"
            const span = document.createElement("span")
            span.textContent = item.name
            div.appendChild(span)
            btn.textContent = "delete"
            btn.addEventListener("click", async () => {
                axios.get(`${url}/post/${item["_id"]}`).then(()=>window.location.reload())
            })
            div.appendChild(btn)
            list.appendChild(div)
        })
    })
})