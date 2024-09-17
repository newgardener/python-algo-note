type primitive = null | boolean | number | string;
type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };

// 1. My Implementation

// function jsonToMatrix(
//   arr: JSONValue[]
// ): (null | boolean | number | string)[][] {
//   const keys = Array.from(new Set(arr.flatMap((obj) => getKeys(obj)))).sort();

//   const matrix = [keys];

//   for (const obj of arr) {
//     const keyToVal: Record<string, primitive> = {};
//     getValues(obj, "", keyToVal);

//     const row: primitive[] = [];
//     keys.forEach((key) => {
//       if (key in keyToVal) {
//         row.push(keyToVal[key]);
//       } else {
//         row.push("");
//       }
//     });
//     matrix.push(row);
//   }

//   return matrix;
// }

// function getKeys(obj: JSONValue, path = "") {
//   if (!isObject(obj)) {
//     return path;
//   }
//   return Object.entries(obj).flatMap(([key, value]) =>
//     getKeys(value, path ? `${path}.${key}` : key)
//   );
// }

// function getValues(
//   obj: JSONValue,
//   path = "",
//   keyToVal: { [key: string]: JSONValue }
// ) {
//   if (Array.isArray(obj)) {
//     obj.forEach((value, index) => {
//       const newPath = path ? `${path}.${index}` : `${index}`;
//       getValues(value, newPath, keyToVal);
//     });
//   } else if (isObject(obj)) {
//     for (const key in obj) {
//       const newPath = path ? `${path}.${key}` : key;
//       getValues(obj[key], newPath, keyToVal);
//     }
//   } else {
//     keyToVal[path] = obj;
//   }
// }

// function isObject(obj: JSONValue): obj is { [key: string]: JSONValue } {
//   return obj !== null && typeof obj === "object";
// }

// 2. Reference

function jsonToMatrix(arr: JSONValue[]): primitive[][] {
  const keys = new Set<string>();
  const rows: Map<string, primitive>[] = [];

  for (const obj of arr) {
    const row = new Map<string, primitive>();

    function traverse(obj: JSONValue, prefix: string = "") {
      if (obj === null) return;

      for (let [key, value] of Object.entries(obj)) {
        key = prefix + key;
        if (value !== null && typeof value === "object") {
          traverse(value, key + ".");
        } else {
          keys.add(key);
          row.set(key, value);
        }
      }
    }

    traverse(obj);

    rows.push(row);
  }

  const keyList = Array.from(keys).sort();

  const result: primitive[][] = [keyList];

  for (const row of rows) {
    result.push(keyList.map((key) => (row.has(key) ? row.get(key)! : "")));
  }

  return result;
}
