type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function jsonToMatrix(arr: JSONValue[]): (null | boolean | number | string)[][] {
    const keyValMap = new Map()
    const matrix = Array.from({ length: arr.length }, () => new Array());
    const rows = Array.from({ length: arr.length }, () => new Array());

    arr.forEach((item, index) => {
        for (const [key, value] of Object.entries(item)) {
            // empty obj
            if (!key && !value) {
                rows[index].push([])
            }
            if (value !== null && typeof value === 'object') {
                // nested obj
                const keyValArr = handleNestedObj(key, value)
                for (const [key, value] of keyValArr) {
                    rows[index].push(key)
                    keyValMap.set(key, [...(keyValMap.get(key) ?? []), value]);
                }

            } else {
                // primitive val
                rows[index].push(key)
                keyValMap.set(key, [...(keyValMap.get(key) ?? []), value]);
            }
        }
    })
    const sortedKeys = [...keyValMap.keys()].sort()
    matrix.unshift(sortedKeys)

    rows.forEach((row, index) => {
        row.forEach((item) => {
            const col = sortedKeys.findIndex(key => key === item)
            const val = keyValMap.get(item).shift()
            matrix[index + 1][col] = val ? val : ""
        })
    })

    return matrix
}

function handleNestedObj(prefix: string, item: JSONValue[] | { [key: string]: JSONValue}) {
    const result = []
    for (const [key, value] of Object.entries(item)) {
        const concatKey = [prefix, key].join(".")
        if (value !== null && typeof value === 'object') {
            result.push(...handleNestedObj(concatKey, value))
        }
        result.push([concatKey, value])
    }
    return result
}