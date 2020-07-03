import React, { useEffect, useState } from 'react'
import { apiTootList, Toot } from '.'

export function TootList(props) {
    const [tootsInit, setTootsInit] = useState([])
    const [toots, setToots] = useState([])
    const [tootsDidSet, setTootsDidSet] = useState(false)

    useEffect(() => {
        const final = [...props.newToots].concat(tootsInit)
        if (final.length !== toots.length) {
            setToots(final)
        }
    }, [props.newToots, tootsInit, toots])

    useEffect(() => {
        if (tootsDidSet === false) {
            const apiTootListCallback = (response, status) => {
                if (status === 200) {
                    setTootsInit(response)
                    setTootsDidSet(true)
                } else {
                    alert(response.message)
                }
            }
            apiTootList(props.username, apiTootListCallback)
        }
    }, [tootsInit, tootsDidSet, setTootsDidSet, props.username])

    const didRetootHandler = (retoot) => {
        const updatedtootsInit = [...tootsInit]
        updatedtootsInit.unshift(retoot)
        setTootsInit(updatedtootsInit)
        console.log(updatedtootsInit)

        const updatedtootsFinal = [...toots]
        updatedtootsFinal.unshift(toots)
        setToots(updatedtootsFinal)
        console.log(updatedtootsFinal)

    }

    return toots.map((toot, index) => {
        return <Toot toot={toot} didRetoot={didRetootHandler} className="col-10 mx-auto my-5 py-5 border rounded bg-white text-dark" key={index} />
    })
}
