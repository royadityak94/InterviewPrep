def balance(s):  # s is a string of '(' and ')' characters in any order
  n = len(s)
  print('original string: %s' % s)

  # Mark all matched pairs
  marked = n * [ False ]
  left_parentheses = []
  for i, ch in enumerate(s):
    if ch == '(':
      left_parentheses.append(i)
    else:
      if len(left_parentheses) != 0:
        marked[i] = True
        marked[left_parentheses.pop()] = True

  # Display the matched pairs and unmatched characters.
  matched, remaining = [], []
  for i, ch in enumerate(s):
    if marked[i]:
      matched.append(ch)
      remaining.append(' ')
    else:
      matched.append(' ')
      remaining.append(ch)
  print('  matched pairs: %s' % ''.join(matched))
  print('      unmatched: %s' % ''.join(remaining))

  cost = 0
  deleted = n * [ False ]
  new_chars = list(s)

  # Balance the unmatched ')' characters.
  right_count, last_right = 0, -1
  for i, ch in enumerate(s):
    if not marked[i] and ch == ')':
      right_count += 1
      if right_count % 2 == 1:
        new_chars[i] = '('
        cost += 1
        last_right = i
  if right_count % 2 == 1:      # Delete the last ')' if we couldn't match it.
    deleted[last_right] = True  # The cost was incremented during replacement.

  # Balance the unmatched '(' characters.
  left_count, last_left = 0, -1
  for i, ch in enumerate(s):
    if not marked[i] and ch == '(':
      left_count += 1
      if left_count % 2 == 0:
        new_chars[i] = ')'
        cost += 1
      else:
        last_left = i
  if left_count % 2 == 1:      # Delete the last '(' if we couldn't match it.
    deleted[last_left] = True  # This character wasn't replaced, so we must
    cost += 1                  # increment the cost now.

  # Display the outcome of replacing and deleting.
  balanced = []
  for i, ch in enumerate(new_chars):
    if marked[i] or deleted[i]:
      balanced.append(' ')
    else:
      balanced.append(ch)
  print('        balance: %s' % ''.join(balanced))

  # Display the cost of balancing and the overall balanced string.
  print('           cost: %d' % cost)
  result = []
  for i, ch in enumerate(new_chars):
    if not deleted[i]:  # Skip deleted characters.
      result.append(ch)
  print('     new string: %s' % ''.join(result))


#balance(')()(()())))()((())((')
# balance('))((')
balance(')())())(')
