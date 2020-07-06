import React, { useState, useEffect } from 'react'
import { ActionBtn } from '.'

export function ParentToot(props) {
    const { toot } = props

    return toot.parent ? <Toot isRetoot retooter={props.retooter} hideAction className="col-11 p-3 mx-auto border rounded" toot={toot.parent} /> : null
}

export function Toot(props) {
    const { toot, didRetoot, hideAction, isDetail, isRetoot, retooter } = props
    const [actionToot, setActionToot] = useState(props.toot ? props.toot : null)
    let className = props.className ? props.className : "col-10 mx-auto col-md-6"
    className = isRetoot === true ? `col-12 mx-auto col-md-12 border rounded` : className
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
        {isRetoot && <p className="small text-muted">Retoot via @{retooter.username}</p>}
        <div className="d-flex">
            <div className="my-1">
                <span
                    className="mx-1 rounded-circle bg-dark text-white display-4"
                    style={{height: 3 + "rem", width: 3 + "rem", display: "inline-block", "textAlign": "center"}}
                >
                    {toot.user.first_name[0]}
                </span>
            </div>
            <div className="col-11">
                <div>
                    <p className="mb-1">{toot.user.first_name} {toot.user.last_name}</p>
                    <p className="small muted">@{toot.user.username}</p>
                    <p>{toot.content}</p>
                    <ParentToot toot={toot} retooter={toot.user}/>
                </div>
                <div className="btn btn-group px-0 mt-3">
                    {(actionToot && hideAction !== true) && <React.Fragment>
                        <ActionBtn toot={actionToot} didPerformAction={performActionhandler} action={{ type: "like", display: "Likes" }} />
                        <ActionBtn toot={actionToot} didPerformAction={performActionhandler} action={{ type: "unlike", display: "Unlike" }} />
                        <ActionBtn toot={actionToot} didPerformAction={performActionhandler} action={{ type: "retoot", display: "Retoot" }} />
                    </React.Fragment>
                    }
                    {isDetail ? null : <button className="btn btn-outline-primary btn-sm" onClick={handleLink}>View Toot</button>}
                </div>
            </div>
        </div>
    </div>
}