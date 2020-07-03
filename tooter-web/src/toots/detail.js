import React, { useState, useEffect } from 'react'
import { ActionBtn } from '.'

export function ParentToot(props) {
    const { toot } = props

    return toot.parent ? <div className="row">
        <p className="col-11 p-3 mx-auto mb-0 text-muted small">Retoot</p>
        <Toot hideAction className="col-11 p-3 mx-auto border rounded" toot={toot.parent} />
    </div> : null
}

export function Toot(props) {
    const { toot, didRetoot, hideAction, isDetail } = props
    const [actionToot, setActionToot] = useState(props.toot ? props.toot : null)
    const className = props.className ? props.className : "col-10 mx-auto col-md-6"
    var [reTootTrigger, setreTootTrigger] = useState(false)

    const performActionhandler = (newActionToot, status) => {
        if (status === 200) {
            setActionToot(newActionToot)
        } else {
            if (didRetoot) {
                didRetoot(newActionToot)
                setreTootTrigger(!reTootTrigger)
            }
        }
    }

    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `/${toot.id}`
    }

    useEffect(() => {
        setActionToot(props.toot)
    }, [props.toot, reTootTrigger])

    return <div className={className}>
        <div>
            <p className="small">{toot.id}</p>
            <p>{toot.content}</p>
            <ParentToot toot={toot} />
        </div>
        <div className="btn btn-group">
            {(actionToot && hideAction !== true) && <React.Fragment>
                <ActionBtn toot={actionToot} didPerformAction={performActionhandler} action={{ type: "like", display: "Likes" }} />
                <ActionBtn toot={actionToot} didPerformAction={performActionhandler} action={{ type: "unlike", display: "Unlike" }} />
                <ActionBtn toot={actionToot} didPerformAction={performActionhandler} action={{ type: "retoot", display: "Retoot" }} />
            </React.Fragment>
            }
            {isDetail ? null : <button className="btn btn-outline-primary btn-sm" onClick={handleLink}>View Toot</button>}
        </div>
    </div>
}