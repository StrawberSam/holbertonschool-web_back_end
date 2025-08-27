export default function cleanSet(set, startString){
  const results = []

  if (startString === '' || typeof startString !== 'string') {
  return '';
  }

  for (let value of set){
    if (value.startsWith(startString)){
      results.push(value.slice(startString.length))
    }
  }
  return results.join('-')
}
