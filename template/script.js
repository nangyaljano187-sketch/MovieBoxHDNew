
"use strict";

/* =========================================
   CineWorld - Main JavaScript
   Frontend ready for future Django backend
========================================= */

document.addEventListener("DOMContentLoaded", () => {
    initMobileMenu();
    initSearch();
    initContentCards();
    initPlayButtons();
});


/* =========================================
   1. MOBILE NAVIGATION MENU
========================================= */

function initMobileMenu() {
    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    if (!menuToggle || !navMenu) return;

    menuToggle.setAttribute("aria-expanded", "false");

    menuToggle.addEventListener("click", () => {
        const isOpen = navMenu.classList.toggle("open");

        menuToggle.setAttribute("aria-expanded", String(isOpen));
    });

    // Close menu after clicking a navigation link
    navMenu.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navMenu.classList.remove("open");
            menuToggle.setAttribute("aria-expanded", "false");
        });
    });

    // Close menu when Escape is pressed
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            navMenu.classList.remove("open");
            menuToggle.setAttribute("aria-expanded", "false");
        }
    });
}


/* =========================================
   2. SEARCH BOX AND CONTENT FILTERING
========================================= */

function initSearch() {
    const searchToggle = document.getElementById("searchToggle");
    const searchBox = document.getElementById("searchBox");
    const searchForm = document.getElementById("searchForm");
    const searchInput = document.getElementById("searchInput");

    if (!searchInput) return;

    // Open and close search box
    if (searchToggle && searchBox) {
        searchToggle.setAttribute("aria-expanded", "false");

        searchToggle.addEventListener("click", () => {
            const isOpen = searchBox.classList.toggle("open");

            searchToggle.setAttribute(
                "aria-expanded",
                String(isOpen)
            );

            if (isOpen) {
                searchInput.focus();
            } else {
                searchInput.value = "";
                filterContent("");
            }
        });
    }

    // Prevent page reload when submitting search
    if (searchForm) {
        searchForm.addEventListener("submit", (event) => {
            event.preventDefault();
            filterContent(searchInput.value);
        });
    }

    // Filter content while typing
    searchInput.addEventListener("input", () => {
        filterContent(searchInput.value);
    });
}


/* =========================================
   3. FILTER MOVIES, VIDEOS AND PICTURES
========================================= */

function filterContent(searchTerm) {
    const cards = document.querySelectorAll(
        ".content-card, .picture-card"
    );

    const query = searchTerm.trim().toLowerCase();

    const sections = new Set();
    let visibleCount = 0;

    cards.forEach((card) => {
        const searchableText = [
            card.innerText || "",
            card.textContent || "",
            card.getAttribute("data-search") || "",
            card.getAttribute("data-title") || "",
            card.getAttribute("data-category") || ""
        ].join(" ").toLowerCase();

        const matches = query === "" || searchableText.includes(query);

        card.hidden = !matches;

        if (matches) {
            visibleCount++;
        }

        const section = card.closest("section");

        if (section) {
            sections.add(section);
        }
    });

    // Hide a section if all its content cards are hidden
    sections.forEach((section) => {
        const sectionCards = section.querySelectorAll(
            ".content-card, .picture-card"
        );

        const hasVisibleCards = Array.from(sectionCards).some(
            (card) => !card.hidden
        );

        section.hidden = !hasVisibleCards;
    });

    // Show a message when no content matches the search
    let noResults = document.getElementById("searchNoResults");

    if (!noResults) {
        noResults = document.createElement("p");
        noResults.id = "searchNoResults";
        noResults.className = "search-no-results";
        noResults.textContent = "Sorry, koi content nahi mila.";
        noResults.setAttribute("role", "status");

        const main = document.querySelector("main");

        if (main) {
            main.appendChild(noResults);
        }
    }

    noResults.hidden = query === "" || visibleCount > 0;
}


/* =========================================
   4. CONTENT CARD INITIALIZATION
========================================= */

function initContentCards() {
    const cards = document.querySelectorAll(
        ".content-card, .picture-card"
    );

    cards.forEach((card) => {
        // Add a fallback accessible label if missing
        if (!card.hasAttribute("tabindex")) {
            card.setAttribute("tabindex", "0");
        }
    });
}


/* =========================================
   5. PLAY BUTTONS
========================================= */

function initPlayButtons() {
    const playButtons = document.querySelectorAll(".play-button");

    playButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            // Avoid accidental card or link navigation
            event.preventDefault();

            const card = button.closest(
                ".content-card, .picture-card"
            );

            if (!card) return;

            const titleElement = card.querySelector(
                "h2, h3, h4, .card-title"
            );

            const title = titleElement
                ? titleElement.textContent.trim()
                : "Selected content";

            /*
              Actual video playback will be connected
              when real video URLs or Django media URLs
              are available.
            */
            console.info(
                "Selected content:",
                title,
                "- Add the real media URL to enable playback."
            );
        });
    });
}
