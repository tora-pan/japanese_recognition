/* eslint-disable @typescript-eslint/no-explicit-any */
import { useState } from "react";

const useLocalStorage = (key: string, defaultValue: any) => {
    // Create state variable to store 
    // localStorage value in state
    const [localStorageValue, setLocalStorageValue] = useState(() => {
        try {
            const value = localStorage.getItem(key)
         
            if (value) {
                return JSON.parse(value)
            } else {
                localStorage.setItem(key, JSON.stringify(defaultValue));
                return defaultValue
            }
        } catch (error: Error | unknown) {
          console.error(error);
            localStorage.setItem(key, JSON.stringify(defaultValue));
            return defaultValue
        }
    })

      const setLocalStorageStateValue = (valueOrFn:any) => {
        let newValue;
        if (typeof valueOrFn === 'function') {
            const fn = valueOrFn;
            newValue = fn(localStorageValue)
        }
        else {
            newValue = valueOrFn;
        }
        localStorage.setItem(key, JSON.stringify(newValue));
        setLocalStorageValue(newValue)
    }
    return [localStorageValue, setLocalStorageStateValue]
}

export default useLocalStorage;