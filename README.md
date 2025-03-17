# WizzAir All You Can Fly Availability Data

WizzAir created a subscription service called [All You Can Fly](https://www.wizzair.com/en-gb/information-and-services/memberships/all-you-can-fly), where subscribers can pay a nominal fix price (10 EUR) for flight tickets booked at most 3 days in advance. However, not all seats or all flights are eligible for the cheap tickets.

From the All You Can Fly **FAQ**:
> [...] flight and seat availability seen in the normal booking flow does not guarantee that the available flights and seats for All You Can Fly members will be the same.

Flight availability data is published every day in the morning (Central European Time), and is publicly available in the PDF format at <https://multipass.wizzair.com/aycf-availability.pdf>

This project aims to record the availability data in an accessible format, `csv`, for analysis. At this time, the earliest datapoint is from `2025-03-16`.

## Disclaimer

The following disclaimer is present in the source PDFs:
> Please note: all the information on this page is correct at the time of its publication (7:00 AM every day).
> If you are trying to book at a later time, the list of available flights may be different.
> Please also note that seats are subject to availability, which depends on several external and internal factors.
> Seat availability seen in the normal booking flow does not guarantee that the available seats for All You Can Fly will be the same. Please review the [Terms & Conditions](https://multipass.wizzair.com/aycf-terms-all.pdf) for more information.

## Goals

- [ ] Create Containerfile to execute using a container runtime (use `uv` + install `camelot` prerequisites)
- Refactor code
  - [ ] Availability PDF URL should be a parameter
  - [ ] Separate functionality of downloading and parsing
  - [ ] Make parsing more bulletproof: handle different timezones in string, clear occasional possible leading/trailing whitespace
- [ ] Automatically execute every day (GitHub Actions?)
- [ ] Choose license(s), possibly different license for the data
