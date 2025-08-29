export default function getFullResponseFromAPI(success){
  const myPromise = new Promise((resolve, reject) => {

    const status = 200
    const body = 'Success'

    if (success){
      resolve({status, body});
    }

    else
      reject (new Error("The fake API is not working currently"));
  })

  return myPromise;
}
