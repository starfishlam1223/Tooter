import { backendLookup } from "../lookup"

export function apiTootCreate(newToot, callback) {
    backendLookup("POST", "toots/create/", callback, { content: newToot })
}

export function apiTootList(username, callback) {
    let endpoint = "toots/"
    if (username) {
        endpoint = `toots/?username=${username}`
    }
    backendLookup("GET", endpoint, callback)
}

export function apiTootAction(id, action, callback) {
    backendLookup("POST", "toots/action/", callback, { id: id, action: action })
}

export function apiTootDetail(id, callback) {
    backendLookup("GET", `toots/${id}/`, callback)
}
