import Data.Char
main = do
    putStrLn "What's your first name?"
    firstName <- getLine
    putStrLn "What's your last name?"
    lastName <- getLine
    let capFirstName = map toUpper firstName
    let capLastName = map toUpper lastName
    print $ "Hey, " ++ capFirstName ++ " " ++ capLastName ++ ", How are you doing today?"
