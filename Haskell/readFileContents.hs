import Control.Monad (when)
import Data.Char (toLower)
import Data.List (sort, group)
import Control.Arrow ((&&&))
import Data.Map (Map)

main = do
    contents <- readFile "newfile.txt"
    putStrLn "The contents of the file are as follows: "
    putStrLn contents
    putStrLn "Implementing the word count algorithm."
    wordCount :: String -> Map String Integer
    wordCount = count.sort.word.preProcess
          where
              preProcess = map toLower.filter ( not.isPunctuation )
              isPunctuation  =flip elem ",.;$^:!&@%"
              count = foldr (\k -> insertWith (+)  k 1 ) empty
