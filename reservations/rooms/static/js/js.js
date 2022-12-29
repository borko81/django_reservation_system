let danger = document.querySelectorAll('.btn-danger')

danger.forEach(x => {
    x.addEventListener("click", (e) => {
        e.preventDefault()

        let href = e.target.getAttribute("href")
        let ask = confirm("Are you sure")
        if (ask) {

            fetch (href)
            .then((response) => response.json())
            .then((data) => location.reload())
            .catch(error => console.error('Error:', error))

        } else {
            console.log("Action stop by user")
        }
    })
})