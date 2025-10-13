---
# the default layout is 'page'
icon: fas fa-pen-to-square
order: 9
published: true
permalink: /contribute
toc: false
image: /assets/img/Contribute.jpg
---

<style>
    pre { white-space: pre-wrap; word-wrap: break-word; }
</style>

<style>
    .contact-form {
      /* max-width: 500px; */
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

# Contributor Guide: How to Share Helpful Information

The **SCHH Knowledge Base** is a growing collection of useful, factual information about life in **Sun City Hilton Head**. It includes official resources and community-sourced notes shared by residents.  

By contributing, you’re helping make the **SCHH AI Assistant** more accurate and useful for everyone — whether it’s answering a quick question or helping someone new find their way around.

---

## What You Can Share

Think of it as *neighbor-to-neighbor knowledge* — something you’d gladly pass along to someone new to the community.

Examples include:

- **How-tos:**  
  How to reserve amenities, submit a modification request, or register a golf cart.
- **Club updates:**  
  Meeting schedules, activity highlights, or event reminders.
- **Tips:**  
  Resident-recommended vendors or helpful insights from experience.
- **Meeting notes:**  
  Summaries from committees or information sessions.
- **Reference info:**  
  Upcoming events, deadlines, or SunSations mentions worth noting.

> *If it’s factual, broadly useful, and not already easy to find, it’s perfect for the Knowledge Base.*
{: .prompt-info}

---

## What Not to Share

To keep the Knowledge Base reliable and respectful, please **don’t include**:

- Personal opinions or complaints  
- Private or identifying information (addresses, phone numbers, emails)  
- Rumors or unverified information  
- Ads, promotions, or solicitations  

> *Our goal is a friendly, factual, and trustworthy community resource.*
{: .prompt-info}

---

## How to Submit

You can share your content as:
  
- a **TeamReach DM** (for short posts)
- by **email** to **info@schh-commons.org** (for longer ones)
- using the **[form below](#contribute-form)**

Use this **simple, natural format** — no special tags, forms, or attachments needed:

```markdown
Title (first line)

1–3 sentences summarizing the key point.

Additional details, steps, or explanation.

source: SunSations Oct 2025 (optional)
```

## Example Submission

```markdown
LATS Transportation Update – October 2025

The LowCountry Area Transportation Study (LATS) plans and coordinates future infrastructure projects in our area. A public session on the Hardeeville portion of Highway 278 is scheduled, and several local traffic-light projects are moving forward.

The Hardeeville meeting will be held Oct 23 at 4 p.m. at the Hardeeville Recreation Center. Lights at Argent & 278 and Sundance & Argent are expected to go out for bid in Nov 2025. Pulte has contributed funding, and Hardeeville has allocated $800,000 for three lights, including Argent & Short Cut Road. Info shared by Joe Passiment, Beaufort County Councilor.

source: TeamReach post, Oct 2025
```

## What Happens Next

Each submission is reviewed for clarity and accuracy before being added to the Knowledge Base.
You don’t need to worry about formatting — AI will handle that part.

Every contribution helps make it easier for residents to find information quickly, and helps build a lasting, community-driven resource for Sun City Hilton Head.

## Contribute Form

<form class="contact-form" action="https://formsubmit.co/info@schh-commons.org" method="POST">
  <label for="name">Name</label>
  <input id="name" type="text" name="name" required>

  <label for="email">Email</label>
  <input id="email" type="email" name="email" required>

  <label for="message">Message</label>
  <textarea id="message" name="message" rows="10" required></textarea>

  <!-- hidden options -->
  <input type="hidden" name="_subject" value="Content Submission">
  <input type="hidden" name="_next" value="https://www.schh-commons.org/thanks">
  <input type="text" name="_honey" style="display:none">
  <input type="hidden" name="_captcha" value="false">

  <button type="submit">Send</button>
</form>
