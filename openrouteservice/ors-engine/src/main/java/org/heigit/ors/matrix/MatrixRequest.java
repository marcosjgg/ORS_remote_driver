/*  This file is part of Openrouteservice.
 *
 *  Openrouteservice is free software; you can redistribute it and/or modify it under the terms of the
 *  GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1
 *  of the License, or (at your option) any later version.

 *  This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 *  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU Lesser General Public License for more details.

 *  You should have received a copy of the GNU Lesser General Public License along with this library;
 *  if not, see <https://www.gnu.org/licenses/>.
 */
package org.heigit.ors.matrix;

import com.graphhopper.routing.weighting.Weighting;
import org.heigit.ors.common.DistanceUnit;
import org.heigit.ors.common.ServiceRequest;
import org.locationtech.jts.geom.Coordinate;

public class MatrixRequest extends ServiceRequest {
    private int profileType = -1;
    private Coordinate[] sources;
    private Coordinate[] destinations;
    private int metrics = MatrixMetricsType.DURATION;
    private int weightingMethod;
    private DistanceUnit units = DistanceUnit.METERS;
    private boolean resolveLocations = false;
    private boolean flexibleMode = false;
    private String algorithm;
    private MatrixSearchParameters searchParameters;
    private double maximumSearchRadius;
    private int maximumVisitedNodes;
    private boolean hasInfiniteUTurnCosts;

    public MatrixRequest(double maximumSearchRadius, int maximumVisitedNodes, double uTurnCost) {
        this.maximumSearchRadius = maximumSearchRadius;
        this.maximumVisitedNodes = maximumVisitedNodes;
        this.hasInfiniteUTurnCosts = uTurnCost == Weighting.INFINITE_U_TURN_COSTS;
    }

    public Coordinate[] getSources() {
        return sources;
    }

    public void setSources(Coordinate[] sources) {
        this.sources = sources;
    }

    public Coordinate[] getDestinations() {
        return destinations;
    }

    public void setDestinations(Coordinate[] destinations) {
        this.destinations = destinations;
    }

    public int getMetrics() {
        return metrics;
    }

    public void setMetrics(int metrics) {
        this.metrics = metrics;
    }

    public boolean getResolveLocations() {
        return resolveLocations;
    }

    public void setResolveLocations(boolean resolveLocations) {
        this.resolveLocations = resolveLocations;
    }

    public int getProfileType() {
        return profileType;
    }

    public void setProfileType(int profile) {
        profileType = profile;
    }

    public DistanceUnit getUnits() {
        return units;
    }

    public void setUnits(DistanceUnit units) {
        this.units = units;
    }

    public int getTotalNumberOfLocations() {
        return destinations.length * sources.length;
    }

    public int getWeightingMethod() {
        return weightingMethod;
    }

    public void setWeightingMethod(int weightingMethod) {
        this.weightingMethod = weightingMethod;
    }

    public boolean getFlexibleMode() {
        return flexibleMode;
    }

    public void setFlexibleMode(boolean flexibleMode) {
        this.flexibleMode = flexibleMode;
    }

    public String getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }

    public double getMaximumSearchRadius() {
        return maximumSearchRadius;
    }

    public void setMaximumSearchRadius(double radius) {
        this.maximumSearchRadius = radius;
    }

    public int getMaximumVisitedNodes() {
        return maximumVisitedNodes;
    }

    public void setMaximumVisitedNodes(int maximumVisitedNodes) {
        this.maximumVisitedNodes = maximumVisitedNodes;
    }

    public void setSearchParameters(MatrixSearchParameters searchParameters) {
        this.searchParameters = searchParameters;
    }

    public MatrixSearchParameters getSearchParameters() {
        return searchParameters;
    }

    public boolean isValid() {
        return !(sources == null && destinations == null);
    }

    public boolean hasInfiniteUTurnCosts() {
        return hasInfiniteUTurnCosts;
    }

    public void setInfiniteUTurnCosts(boolean hasInfiniteUTurnCosts) {
        this.hasInfiniteUTurnCosts = hasInfiniteUTurnCosts;
    }
}
