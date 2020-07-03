import React from 'react'
import { apiTootCreate } from '.'

export function TootCreate(props) {
    const textAreaRef = React.createRef()
    const { didToot } = props
    const createTootCallback = (response, status) => {
        if (status === 201) {
            didToot(response)
        } else {
            alert("Your toot cannot be created")
        }
    }

    const submitHandler = (event) => {
        event.preventDefault()
        const tootContent = textAreaRef.current.value
        apiTootCreate(tootContent, createTootCallback)
        textAreaRef.current.value = ""
    }

    return <div className={props.className}>
        <form className="form" id="toot-create-form" onSubmit={submitHandler}>
            <textarea ref={textAreaRef} required className="form-control" name="content" placeholder="What is your toot today?"></textarea>
            <button type="submit" className="btn btn-primary my-3">Toot</button>
        </form>
    </div>
}
