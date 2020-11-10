function displayCommentRow() {
    document.querySelector("#new-comment-row").style.display = "block" // Show the comment form
    document.querySelector('#new-comment-button').style.display = "none" // Hide the new comment button
    document.querySelector('#less-comment-button').style.display = "block" // Show the less button
    document.querySelector('#commentsHeader').scrollIntoView()
}
function hideCommentRow() {
    document.querySelector("#new-comment-row").style.display = "none"
    document.querySelector('#new-comment-button').style.display = "block" // Show the new comment button
    document.querySelector('#less-comment-button').style.display = "none" // Hide the less button
}

function getCommentInfo() {
    const url = window.location.href
    const split = url.split('/')
    const isbn = split[split.length-1]

    parentReview = isbn
    commenterName = document.querySelector('#commenter-name').value
    commenterEmail = document.querySelector('#commenter-email').value
    commentBody = document.querySelector('#comment-body').value

    comment = {
        parentReview: parentReview,
        commenterName: commenterName,
        commenterEmail: commenterEmail,
        commentBody: commentBody,
    }

    return comment
}

function postComment() {

  const comment = getCommentInfo()

  fetch('/post-comment/', {
    method: "POST",
    body: JSON.stringify({comment: comment})
  })
  .then(response => response.json())
  .then(result => {
    // TODO: Append the comment
    location.reload()
  })
}

// DOM Content Loaded Configuration
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#new-comment-button').onclick = displayCommentRow
    document.querySelector('#less-comment-button').onclick = hideCommentRow
    document.querySelector('#submit-comment-button').onclick = postComment
})