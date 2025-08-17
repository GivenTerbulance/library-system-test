async function postData(url, data) {
    const res = await fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    return res.json();
}

document.getElementById("bookForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target).entries());
    const res = await postData("/add_book", data);
    alert(res.status === "success" ? "Book added!" : res.message);
});

document.getElementById("memberForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target).entries());
    const res = await postData("/register_member", data);
    alert(res.status === "success" ? "Member registered!" : res.message);
});

document.getElementById("borrowForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target).entries());
    const res = await postData("/borrow_book", data);
    alert(res.status === "success" ? "Book borrowed!" : res.message);
});

document.getElementById("returnForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target).entries());
    const res = await postData("/return_book", data);
    alert(res.status === "success" ? "Book returned!" : res.message);
});

document.getElementById("loadBooks").addEventListener("click", async () => {
    const res = await fetch("/list_books");
    const books = await res.json();
    const list = document.getElementById("booksList");
    list.innerHTML = "";
    books.forEach(b => {
        const li = document.createElement("li");
        li.textContent = `${b.title} by ${b.author} (${b.copies} copies)`;
        list.appendChild(li);
    });
});
