import unittest
from unittest.mock import MagicMock, patch
import datetime as dt
import pytz
from GenerateMeetingInviteDraft import datetime_to_ole, create_draft_meeting_invite_local


class TestYourModule(unittest.TestCase):

    def test_datetime_to_ole(self):
        dt_obj = dt.datetime(2023, 6, 26, 15, 0, tzinfo=pytz.UTC)
        ole_date = datetime_to_ole(dt_obj)
        self.assertEqual(ole_date, "06/26/2023 15:00:00")

    @patch('GenerateMeetingInviteDraft.win32com.client.Dispatch')
    def test_create_draft_meeting_invite_local(self, mock_dispatch):
        # Set up mock objects
        mock_outlook_app = MagicMock()
        mock_appointment = MagicMock()
        mock_outlook_app.CreateItem.return_value = mock_appointment
        mock_dispatch.return_value = mock_outlook_app

        # Test data
        subject = "Team Meeting"
        start_datetime = dt.datetime(2023, 6, 26, 15, 0, tzinfo=pytz.UTC)
        end_datetime = dt.datetime(2023, 6, 26, 16, 0, tzinfo=pytz.UTC)
        location = "Meeting Room 1"
        body_text = "This is to discuss our upcoming project."
        recipients = ["klaus.haeuptle@sap.com", "priya.singh05@sap.com"]
        organizer_email = "klaus.haeuptle@sap.com"

        # Call function
        create_draft_meeting_invite_local(subject, start_datetime, end_datetime, location, body_text, recipients, organizer_email)

        # Check that Outlook application and appointment were created
        mock_dispatch.assert_called_once_with('Outlook.Application')
        mock_outlook_app.CreateItem.assert_called_once_with(1)

        # Check that appointment properties were set
        self.assertEqual(mock_appointment.Subject, subject)
        self.assertEqual(mock_appointment.Start, "06/26/2023 15:00:00")
        self.assertEqual(mock_appointment.End, "06/26/2023 16:00:00")
        self.assertEqual(mock_appointment.Body, body_text)

        # Check that recipients were added
        self.assertEqual(mock_appointment.Recipients.Add.call_count, len(recipients) + 1)  # Add 1 for the organizer

        # Check that the draft meeting invite was displayed
        mock_appointment.Display.assert_called_once_with(True)


if __name__ == "__main__":
    unittest.main()
