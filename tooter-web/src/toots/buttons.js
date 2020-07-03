import React from 'react'
import { apiTootAction } from '.'

export function ActionBtn(props) {
    const { toot, action, didPerformAction } = props
    const likeCount = toot.likeCount ? toot.likeCount : 0
    const className = props.className ? props.className : "btn btn-primary btn-sm"
    const actionDisplay = action.display ? action.display : "Action"
    const display = action.type === "like" ? `${likeCount} ${actionDisplay}` : actionDisplay

    const apiTootActionCallback = (response, status) => {
        if ((status === 200 || status === 201) && didPerformAction) {
            didPerformAction(response, status)
        }
        // if (action.type === "like") {
        // } else if (action.type === "unlike") {

        // } else if (action.type === "retoot") {

        // }
    }

    const handleClick = (event) => {
        event.preventDefault()
        apiTootAction(toot.id, action.type, apiTootActionCallback)
    }

    return <button className={className} onClick={handleClick}>
        {display}
    </button>
}