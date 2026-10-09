'''Question 5: Social Media Likes 
A social media platform stores the number of likes received by five 
posts in a list. Write a function to find the post with the highest 
likes, calculate total likes, and display posts that received at least 
100 likes.'''


def analze_likes(likes):
    print(f"Highest likes is: {max(likes)}")
    print(f"Total   likes is: {sum(likes)}")
    print(f"This like is greaterthan 100: {[   i for i in likes if i>=100]}")




analze_likes([23,57,1000,600,400,234])
  