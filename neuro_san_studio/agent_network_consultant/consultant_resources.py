# Copyright © 2025-2026 Cognizant Technology Solutions Corp, www.cognizant.com.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# END COPYRIGHT

"""Resources that require cleanup after a consultant run."""


class ConsultantResources:
    """Manage in-memory fixture-ratio overrides for a Consultant run."""

    def __init__(self) -> None:
        """Initialize empty cleanup state."""
        self._success_ratio_overrides: dict[str, str] = {}

    def success_ratio_overrides(self) -> dict[str, str]:
        """
        Return an isolated copy of fixture execution overrides.

        :return: Success ratios keyed by fixture basename.
        """
        return dict(self._success_ratio_overrides)

    def has_success_ratio_overrides(self) -> bool:
        """
        Return whether confidence handling selected stricter fixture ratios.

        :return: Whether any in-memory success-ratio overrides are active.
        """
        return bool(self._success_ratio_overrides)

    def remember_success_ratio_overrides(self, fixture_names: list[str], ratio: str) -> None:
        """
        Retain stricter ratios for subsequent executions of selected fixtures.

        :param fixture_names: Fixture basenames selected for stricter verification.
        :param ratio: The success ratio to use for those fixture executions.
        """
        for fixture_name in fixture_names:
            self._success_ratio_overrides[fixture_name] = ratio
