type primitive = null | boolean | number | string;
type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };

function jsonToMatrix(
  arr: JSONValue[]
): (null | boolean | number | string)[][] {
  const keys = Array.from(new Set(arr.flatMap((obj) => getKeys(obj)))).sort();

  const matrix = [keys];

  for (const obj of arr) {
    const keyToVal: Record<string, primitive> = {};
    getValues(obj, "", keyToVal);

    const row: primitive[] = [];
    keys.forEach((key) => {
      if (key in keyToVal) {
        row.push(keyToVal[key]);
      } else {
        row.push("");
      }
    });
    matrix.push(row);
  }

  return matrix;
}

function getKeys(obj: JSONValue, path = "") {
  if (!isObject(obj)) {
    return path;
  }
  return Object.entries(obj).flatMap(([key, value]) =>
    getKeys(value, path ? `${path}.${key}` : key)
  );
}

function getValues(
  obj: JSONValue,
  path = "",
  keyToVal: { [key: string]: JSONValue }
) {
  if (Array.isArray(obj)) {
    obj.forEach((value, index) => {
      const newPath = path ? `${path}.${index}` : `${index}`;
      getValues(value, newPath, keyToVal);
    });
  } else if (isObject(obj)) {
    for (const key in obj) {
      const newPath = path ? `${path}.${key}` : key;
      getValues(obj[key], newPath, keyToVal);
    }
  } else {
    keyToVal[path] = obj;
  }
}

function isObject(obj: JSONValue): obj is { [key: string]: JSONValue } {
  return obj !== null && typeof obj === "object";
}
