import React, { useState, useEffect } from 'react'
import { Toot, TootList, TootCreate } from '.'
import { apiTootDetail } from '.'

export function TootsComponent(props) {
    const canToot = props.canToot === "true"
    const [newToots, setNewToots] = useState([])
    const didToot = (newToot) => {
        let tempNewToots = [...newToots]
        tempNewToots.unshift(newToot)
        setNewToots(tempNewToots)
    }
    return <div className={props.className}>
        {canToot && <TootCreate className="col-12 mb-3" didToot={didToot} />}
        <TootList {...props} newToots={newToots} />
    </div>
}

// export function TootForm(props) {
//     const textAreaRef = React.createRef()
//     const [newToots, setNewToots] = useState()
//     const submitHandler = function (event) {
//         event.preventDefault()
//         let tempNewToots = [...newToots]
//         tempNewToots.unshift({
//             content: textAreaRef.current.value,
//             likecount: 0,
//             id: -1
//         })
//         setNewToots(tempNewToots)
//         textAreaRef.current.value = ""
//     }

//     return <div className="col-12 mb-3">
//         <form className="form" id="toot-create-form" onSubmit={submitHandler}>
//             <textarea required class="form-control" name="content" placeholder="What is your toot today?"></textarea>
//             <button type="submit" class="btn btn-primary my-3">Toot</button>
//         </form>
//     </div>
// }
export function TootDetailComponent(props) {
    const {tootId} = props
    const [didLookup, setDidLookup] = useState(false)
    const [toot, setToot] = useState(null)

    const backendLookupHandler = (response, status) => {
        if (status === 200) {
            setToot(response)
        } else {
            alert("There was an error finding your toot!")
        }
    }
    useEffect(() => {
        if (didLookup === false) {
            apiTootDetail(tootId, backendLookupHandler)
            setDidLookup(true)
        }
    }, [tootId, didLookup, setDidLookup])

    return toot !== null ? <Toot isDetail toot={toot} className={props.className} /> : null
}