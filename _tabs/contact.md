---
# the default layout is 'page'
title: Contact
icon: fas fa-envelope
layout: page
order: 5
---

<style>
    .contact-form {
  max-width: 500px;
  margin: 2rem auto;
  padding: 1.5rem;
  background: #fdfdfd;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.05);
  font-family: system-ui, sans-serif;
}

.contact-form label {
  display: block;
  margin-bottom: 0.3rem;
  font-weight: 600;
  color: #333;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 0.7rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  box-sizing: border-box;
}

.contact-form input:focus,
.contact-form textarea:focus {
  outline: none;
  border-color: #3aa0a0; /* coastal teal accent */
  box-shadow: 0 0 0 3px rgba(58,160,160,0.2);
}

.contact-form button {
  display: inline-block;
  background: #3aa0a0; /* coastal teal accent */
  color: white;
  font-size: 1rem;
  font-weight: 600;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease-in-out;
}

.contact-form button:hover {
  background: #317c7c;
}
</style>

<form class="contact-form" action="https://formsubmit.co/admin@schh-commons.org" method="POST">
  <label for="name">Name</label>
  <input id="name" type="text" name="name" required>

  <label for="email">Email</label>
  <input id="email" type="email" name="email" required>

  <label for="message">Message</label>
  <textarea id="message" name="message" rows="6" required></textarea>

  <!-- hidden options -->
  <input type="hidden" name="_subject" value="Website contact form">
  <input type="hidden" name="_next" value="https://www.schh-commons.org/thanks">
  <input type="text" name="_honey" style="display:none">
  <input type="hidden" name="_captcha" value="false">

  <button type="submit">Send</button>
</form>