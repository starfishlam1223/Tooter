import { backendLookup } from "../lookup"

export function apiTootCreate(newToot, callback) {
    backendLookup("POST", "toots/create/", callback, { content: newToot })
}

export function apiTootList(username, callback, paginationUrl) {
    let endpoint = "toots/"
    if (username) {
        endpoint = `toots/?username=${username}`
    }
    if (paginationUrl !== null && paginationUrl !== undefined) {
        endpoint = paginationUrl.replace("http://localhost:8000/api/", "")
    }
    backendLookup("GET", endpoint, callback)
}

export function apiTootAction(id, action, callback) {
    backendLookup("POST", "toots/action/", callback, { id: id, action: action })
}

export function apiTootDetail(id, callback) {
    backendLookup("GET", `toots/${id}/`, callback)
}
